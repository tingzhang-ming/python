from collections import OrderedDict
import os
import re
import logging as log
import socket
import time
import subprocess
import mysql.connector as mysqlconn
from mysql.connector import Error as MySQLError


class WaitTimeoutError(Exception):
    """ Exception raised when a timeout occurs. """
    pass


class MySQL(object):
    """
    MySQL represents the connection to and configuration of the MySQL
    process and its clients.
    """
    def __init__(self, envs=os.environ):
        self.repl_user = "repluser"
        self.repl_password = "repl.123"
        self._conn = None
        self._query_buffer = OrderedDict()

    @property
    def server_id(self):
        """ replace server-id with ID derived from hostname """
        _hostname = socket.gethostname()
        return int(str(_hostname)[:4], 16)

    def _get_innodb_buffer_pool_size(self):
        """
        replace innodb_buffer_pool_size value from environment
        or use a sensible default (70% of available physical memory)
        """
        if not self.pool_size:
            with open('/proc/meminfo', 'r') as memInfoFile:
                memInfo = memInfoFile.read()
                base = re.search(r'^MemTotal: *(\d+)', memInfo).group(1)
                self.pool_size = int((int(base) / 1024) * 0.7)
        return self.pool_size

    @property
    def conn(self):
        """
        Convenience method for setting up a cached connection
        with the replication manager user.
        """
        if self._conn:
            return self._conn
        ctx = dict(user=self.repl_user,
                   password=self.repl_password,
                   timeout=25) # derived from ContainerPilot config ttl
        self._conn = self.wait_for_connection(**ctx)
        return self._conn

    def wait_for_connection(self, user='root', password=None, database=None,
                            timeout=10):
        """
        Polls mysqld socket until we get a connection or the timeout
        expires (raise WaitTimeoutError). Defaults to root empty/password.
        """
        while timeout > 0:
            try:
                sock = '/var/run/mysqld/mysqld.sock'
                return mysqlconn.connect(
                                         # unix_socket=sock,
                                         host='10.254.35.205',
                                         user=user,
                                         password=password,
                                         database=database,
                                         charset='utf8',
                                         connection_timeout=timeout,
                                         port=3306)
            except MySQLError as ex:
                timeout = timeout - 1
                if timeout == 0:
                    raise WaitTimeoutError(ex)
                time.sleep(1)

    def add(self, stmt, params=()):
        """ Adds a new SQL statement to an internal query buffer """
        self._query_buffer[stmt] = params

    def execute(self, sql, params=(), conn=None):
        """ Execute and commit a SQL statement with parameters """
        self.add(sql, params)
        self._execute(conn, discard_results=True)

    def execute_many(self, conn=None):
        """
        Execute and commit all previously `add`ed statements
        in the query buffer
        """
        self._execute(conn, discard_results=True)

    def query(self, sql, params=(), conn=None):
        """ Execute a SQL query with params and return results. """
        self.add(sql, params)
        return self._execute(conn=conn)

    def _execute(self, conn=None, discard_results=False):
        """
        Execute and commit all composed statements and flushes the buffer
        """
        try:
            if not conn:
                conn = self.conn
        except (WaitTimeoutError, MySQLError):
            raise
        try:
            cur = conn.cursor(dictionary=True, buffered=True)
            for stmt, params in self._query_buffer.items():
                log.debug('%s %s', stmt, params)
                cur.execute(stmt, params=params)
                if not discard_results:
                    return cur.fetchall()

                # we discard results from writes
                conn.commit()
                try:
                    cur.fetchall()
                except MySQLError:
                    # Will get "InternalError: No result set to fetch from."
                    # for SET statements. We can safely let this slide if the
                    # `execute` call passes
                    pass
        finally:
            # exceptions are an unrecoverable situation
            self._query_buffer.clear()
            cur.close()

    def query_errant_transactions(self, ip, port=3306, timeout=10):
        conn = None
        while timeout > 0:
            try:
                conn = mysqlconn.connect(host=ip,
                                         port=port,
                                         user=self.repl_user,
                                         password=self.repl_password,
                                         charset='utf8',
                                         connection_timeout=timeout)
                break
            except MySQLError:
                timeout = timeout - 1
                if timeout == 0:
                    return set()
                time.sleep(1)
        result = self.query('show slave status;', conn=conn)
        if not result or len(result) == 0 or 'Executed_Gtid_Set' not in result[0]:
            return set()
        executed_gtid_set = result[0]['Executed_Gtid_Set']
        executed_gtid_sets = executed_gtid_set.split(',\n')
        if len(executed_gtid_sets) == 0:
            return set()
        retrieved_gtid_set = result[0]['Retrieved_Gtid_Set']
        retrieved_gtid_sets = [r for r in retrieved_gtid_set.split(',\n') if r]
        if len(retrieved_gtid_sets) == 0:
            para2s = executed_gtid_sets[-1].split(':')[0]
        else:
            para2s = retrieved_gtid_sets[0].split(':')[0]
        print para2s
        para2 = [r for r in executed_gtid_sets if para2s in r]
        print para2
        if len(para2) > 0:
            para = para2[0]
        else:
            para = executed_gtid_sets[-1]
        print para
        sql = "select gtid_subtract('%s','%s') as errand" % (','.join(executed_gtid_sets), para)
        result = self.query(sql, conn=conn)
        if not result or len(result) == 0 or 'errand' not in result[0]:
            return set()
        conn.close()
        res = result[0]['errand'].split(',\n')
        print res
        print '---------------'
        return set([r for r in res if r])

    def mysqlslavetrx(self, ips=None, ports=None):
        errands = set()
        if ips is not None:
            port = 3306
            for ip in ips:
                errands |= self.query_errant_transactions(ip, port=port)
            paras = ['%s:%s@%s:%s' % (self.repl_user, self.repl_password, ip, str(port)) for ip in ips]
        elif ports is not None:
            ip = 'localhost'
            for port in ports:
                errands |= self.query_errant_transactions(ip, port=port)
            paras = ['%s:%s@%s:%s' % (self.repl_user, self.repl_password, ip, str(port)) for port in ports]
        else:
            return
        print errands
        cmd = "mysqlslavetrx --gtid-set=%s --slaves=%s" % (','.join(errands), ','.join(paras))
        print cmd
        # log.debug('Execute command: %s', cmd)
        # try:
        #     subprocess.check_call(cmd, shell=True)
        # except subprocess.CalledProcessError:
        #     log.error('Command execute failed: %s', cmd)
        # else:
        #     log.info('Command execute success: %s', cmd)
        return


def t1():
    c = MySQL()
    c.mysqlslavetrx(ports=[33337, 33340])


def t2():
    c = MySQL()
    result = c.query('show status like "wsrep_cluster_status";')
    print result[0]['Value']


def t3():
    c = MySQL()
    to_time = "{} 00:00:00".format(time.strftime("%Y-%m-%d", time.localtime()))
    c.execute(sql="purge master logs before'%s'" % to_time)


if __name__ == '__main__':
    t3()
