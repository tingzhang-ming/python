""" Import/export data by mysqldump/mysql shell client """
from datetime import datetime
from os.path import join
import string
import urllib
import mysql.connector
from dbelt.managers.mysql.ms.manager.utils import Enum, run_shell, log, safe_mkdir
from dbelt.managers.mysql.ms.manager.env import DUMP_NAME, DUMP_DIR


DUMP_ACTION = Enum(["import_data", "export_data"])


class UnsupportActionError(Exception):
    """ Unsupport Action Error """
    pass


class DownloadError(Exception):
    """ Download data Error """
    pass


class MysqlDump(object):
    """ Import/export data by mysqldump/mysql shell client """

    def __init__(self, client, action, parameters, file_name=None, storage=None):
        self._client = client
        self._parameters = parameters
        self._dump_cmd = "mysqldump -uroot -p%s --set-gtid-purged=OFF --opt" \
                         % self._client.mysql_root_password
        self._mysql_cmd = "mysql -uroot -p%s" % self._client.mysql_root_password
        self._file_name = file_name
        self._action = action
        self._storage = storage
        safe_mkdir(DUMP_DIR)

    @property
    def data_file(self):
        """ return output file path """
        if not self._file_name:
            now = datetime.utcnow()
            self._file_name = now.strftime('{}.gz'.format(DUMP_NAME))
        return join(DUMP_DIR, self._file_name)

    @staticmethod
    def _run_cmd(cmd):
        """ run shell command and parse stderr """
        log.debug("execute cmd: %s", cmd)
        _, err = run_shell(cmd)
        result = ""
        if err != "":
            for e in err.split("\n"):
                if '[Warning]' in e:
                    continue
                if e.startswith("mysqldump:"):
                    result += e.split("mysqldump:")[1].strip() + '\n'
                if e.startswith("ERROR"):
                    result += e + '\n'
        return result.strip()

    @staticmethod
    def _parse_uri(uri):
        """ parse download uri """
        if "ftp://" not in uri and \
                "http://" not in uri and \
                "manta://" not in uri:
            raise DownloadError("Expecting 'ftp://' or 'http://' at the beginning of the URL")
        try:
            file_name = string.split(uri, '/')[-1]
        except ValueError:
            raise DownloadError("can not get file name from %s" % uri)
        return file_name

    @staticmethod
    def clear():
        """ clear DUMP_DIR """
        safe_mkdir(DUMP_DIR, clean=True)

    def download(self, uri):
        """ download  data, support manta, ftp, http """
        file_name = self._parse_uri(uri)
        if "manta" in uri:
            self._storage.get_dump(file_name)
        else:
            try:
                local = join(DUMP_DIR, file_name)
                urllib.urlretrieve(uri, local)
                log.info('successfully download %s from %s', file_name, uri)
            except Exception:
                self.clear()
                raise DownloadError('%s can be downloaded from %s ' % (file_name, uri))
        self._file_name = file_name

    def upload(self):
        """ upload dump file """
        self._storage.put_dump(self._file_name, self.data_file)

    def _end_with_gz(self):
        """ return whether end with .gz """
        try:
            return self.data_file.split(".")[-1] == 'gz'
        except (IndexError, ValueError):
            return False

    def _get_export_cmd(self, cmd):
        """ get command to export data. """
        if not self._end_with_gz():
            result = "%s > %s" % (cmd, self.data_file)
        else:
            result = "%s | gzip > %s" % (cmd, self.data_file)
        return result

    def export_data_all(self):
        """ export all databases data """
        cmd = "%s --all-databases" % self._dump_cmd
        return self._run_cmd(self._get_export_cmd(cmd))

    def export_data_database(self, db_name):
        """ export a database data """
        cmd = "%s %s" % (self._dump_cmd, db_name)
        return self._run_cmd(self._get_export_cmd(cmd))

    def export_data_databases(self, db_names):
        """ export multiple databases data """
        cmd = "%s --databases" % self._dump_cmd
        for db_name in db_names:
            cmd += " {}".format(db_name)
        return self._run_cmd(self._get_export_cmd(cmd))

    def export_data_table(self, db_name, table_name):
        """ export a table data in a database """
        cmd = "%s %s %s" % (self._dump_cmd, db_name, table_name)
        return self._run_cmd(self._get_export_cmd(cmd))

    def export_data_tables(self, db_name, table_names):
        """ export multiple tables data in a database """
        cmd = "%s %s" % (self._dump_cmd, db_name)
        for table_name in table_names:
            cmd += " {}".format(table_name)
        return self._run_cmd(self._get_export_cmd(cmd))

    def _get_import_cmd(self, cmd):
        """ get command to import data. """
        if not self._end_with_gz():
            result = "%s < %s" % (cmd, self.data_file)
        else:
            result = "gunzip < %s | %s" % (self.data_file, cmd)
        return result

    def import_data(self):
        """ import data to mysql """
        return self._run_cmd(self._get_import_cmd(self._mysql_cmd))

    def import_data_database(self, db_name):
        """ import data to a database """
        try:
            self._client.execute("create database if not exists %s;" % db_name)
        except mysql.connector.errors.ProgrammingError:
            return "Database '%s' can't be created." %db_name
        cmd = "%s %s" % (self._mysql_cmd, db_name)
        return self._run_cmd(self._get_import_cmd(cmd))

    def run(self):
        """
        export all databases task:
        {"Action":"export_data","Parameters":{"database":"all"},"Status":"prepare"}
        export a database task:
        {"Action":"export_data","Parameters":{"database":"db_name"},"Status":"prepare"}
        export multiple databases task:
        {"Action":"export_data","Parameters":{"database":["db1","db2"]},"Status":"prepare"}
        export a table task:
        {"Action":"export_data","Parameters":{"database":"db","table":"tb"},"Status":"prepare"}
        export multi tables task:
        {"Action":"export_data","Status":"prepare",
        "Parameters":{"database":"db","table":["tb1","tb2"]}}
        import data task:
        {"Action":"import_data","Status":"prepare", "Parameters":{"file_name":"test1-mysql-dump-2017-11-28T03-08-49Z.gz", "database":""}}
        """
        err = ""
        if not isinstance(self._parameters, dict):
            raise KeyError("parameters should be a map")
        if 'file_name' in self._parameters:
            self._file_name = self._parameters['file_name']
        if self._action == DUMP_ACTION.import_data:
            if 'url' not in self._parameters:
                raise KeyError("parameters should be a map like {url:*, database:*}")
            self.download(self._parameters['url'])
            if 'database' not in self._parameters or not self._parameters['database']:
                err = self.import_data()
            else:
                err = self.import_data_database(self._parameters['database'])
            self.clear()
        elif self._action == DUMP_ACTION.export_data:
            if 'database' not in self._parameters:
                raise KeyError("parameters should be a map like {database:*, table:*}")
            if 'table' not in self._parameters:
                if isinstance(self._parameters['database'], basestring):
                    if not self._parameters['database'] or \
                                    self._parameters['database'].lower() == "all":
                        # all databases
                        err = self.export_data_all()
                    else:
                        # a database
                        err = self.export_data_database(self._parameters['database'].lower())
                elif isinstance(self._parameters['database'], list):
                    # multiple databases
                    err = self.export_data_databases(self._parameters['database'])
                else:
                    raise KeyError("database should be a string or list type")
            else:
                if not isinstance(self._parameters['database'], basestring):
                    raise KeyError("database should be a string type")
                if isinstance(self._parameters['table'], basestring):
                    # a table
                    err = self.export_data_table(self._parameters['database'],
                                                 self._parameters['table'])
                elif isinstance(self._parameters['table'], list):
                    # multiple tables in a database
                    err = self.export_data_tables(self._parameters['database'],
                                                  self._parameters['table'])
                else:
                    raise KeyError("table should be a string or list type")
            if not err:
                self.upload()
            self.clear()
        else:
            raise UnsupportActionError("%s acton is unsupported." % self._action)
        return err
