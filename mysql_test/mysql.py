#!/usr/bin/python
import sys
import random
import MySQLdb
from optparse import OptionParser


def get_list(table):
    result = []
    for raw in table:
        for element in raw:
            result.append(element)
    return result


def get_value():
    seed = "1234567890abcdefghijklmnopqrstuvwxyz"
    sa = []
    for i in range(5):
        sa.append(random.choice(seed))
    salt = ''.join(sa)
    return salt


parser = OptionParser()
parser.add_option("-H",
                  dest="host",
                  default="localhost",
                  help="ip of mysql server")
parser.add_option("-P",
                  dest="port",
                  type=int,
                  default=3306,
                  help="port of mysql server")
parser.add_option("-u",
                  dest="user",
                  default="root",
                  help="user name of mysql")
parser.add_option("-p",
                  dest="password",
                  default="root.123",
                  help="password of mysql user")
parser.add_option("--database",
                  dest="database",
                  default='test_database',
                  help="database name")
parser.add_option("--table",
                  dest="table",
                  default='test_table',
                  help="table name")
parser.add_option("--number",
                  dest="number",
                  default=5,
                  type=int,
                  help="line number")

(options, args) = parser.parse_args()

if not options.host or not options.port or not options.user or not options.password:
    print "-H, -P, -u, -p is needed."
    sys.exit(1)


def act():
    conn = MySQLdb.connect(
        host=options.host,
        port=options.port,
        user=options.user,
        passwd=options.password
    )

    cur = conn.cursor()
    a = cur.execute("show databases;")
    databases_table = cur.fetchmany(a)
    databases = get_list(databases_table)

    if options.database not in databases:
        cur.execute("create database %s;" % options.database)

    cur.execute("use %s;" % options.database)

    a = cur.execute("show tables;")
    tables_table = cur.fetchmany(a)
    tables = get_list(tables_table)
    if options.table not in tables:
        cur.execute("create table %s"
                    "(id int,"
                    "attribute1 varchar(20),"
                    "attribute2 varchar(20), "
                    "attribute3 varchar(20),"
                    "attribute4 varchar(20),"
                    "attribute5 varchar(20),"
                    "attribute6 varchar(20),"
                    "attribute7 varchar(20),"
                    "attribute8 varchar(20),"
                    "attribute9 varchar(20));"
                    % options.table)

    a = cur.execute("select MAX(id) from %s;" % options.table)
    max_number = cur.fetchmany(a)

    max_number = get_list(max_number)[0]

    if max_number:
        startnumber = int(max_number)
    else:
        startnumber = 0

    for i in xrange(startnumber, options.number + startnumber):
        sqli = "insert into %s values(%d,'%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (options.table, i + 1,
                                                                                           get_value(),
                                                                                           get_value(),
                                                                                           get_value(),
                                                                                           get_value(),
                                                                                           get_value(),
                                                                                           get_value(),
                                                                                           get_value(),
                                                                                           get_value(),
                                                                                           get_value())
        cur.execute(sqli)

    cur.close()
    conn.commit()
    conn.close()


if __name__ == '__main__':
    act()

