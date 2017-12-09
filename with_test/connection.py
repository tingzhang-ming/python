from contextlib import closing
import psycopg2


class DBConnection(object):

    def __init__(self, dbname=None, user=None,
                 password=None, host='localhost'):
        self.host = host
        self.dbname = dbname
        self.user = user
        self.password = password

    def __enter__(self):
        self.connection = psycopg2.connect(
            dbname=self.dbname,
            host=self.host,
            user=self.user,
            password=self.password
        )
        return self.connection.cursor()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()


def t1():
    with DBConnection(user='root', dbname='foo') as db:
        db.execute('select 1 + 1')
        db.fetchall()


def create_connection(dbname=None, user=None,
                 password=None, host='localhost'):
    connection = psycopg2.connect(
        dbname=dbname,
        host=host,
        user=user,
        password=password
    )
    return connection.cursor()


def t2():
    with closing(create_connection(user='root', dbname='foo')) as db:
        db.execute('select 1 + 1')
        db.fetchall()
