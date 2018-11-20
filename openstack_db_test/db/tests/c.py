from db import get_db_api
from db.data_models.test1 import DBTestTable2


options = dict(
    sql_connection="mysql://root:123@ali:3306/db_test",
    opts={}
)

db_api = get_db_api()


def t1():
   pass


def config():
    db_api.configure_db(options)