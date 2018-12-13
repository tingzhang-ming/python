# encoding: utf-8
from db import get_db_api
from db.data_models.test1 import DBTestTable1

options = dict(
    sql_connection="mysql://root:123@ali:3306/db_test",
    opts={}
)

db_api = get_db_api()


def config():
    db_api.configure_db(options)


def t1():
    db_api.db_sync(options, version=3)


def t2():
    config()
    test1 = DBTestTable1.create(
        name="name2",
        description="description1"
    )
    print test1.id


def t3():
    config()
    test1 = DBTestTable1.get_by(id="e33d0153-ec85-4731-bc87-73f818017dbd")
    print test1.name
    print test1.description


def t4():
    config()
    test1 = DBTestTable1.find_all(name="name1")
    print type(test1)
    f1 = test1.first()
    print f1.name
    fs = test1.all()
    print type(fs)
    print test1.count()
# <class 'db.Query'>
# name1
# <type 'list'>
# 2

# 442a0ef0-4c82-45a4-9985-074a6c531e28	2018-11-16 17:33:35	2018-11-16 17:33:35	name2	description1
# b9159d4b-43bb-4876-b1df-304cc2d93364	2018-11-16 17:21:25	2018-11-16 17:21:25	name1	description2
# e33d0153-ec85-4731-bc87-73f818017dbd	2018-11-16 17:21:51	2018-11-16 17:21:51	name1	description1


def t5():
    config()
    test1 = DBTestTable1.find_all()
    print test1.count()
    fs = test1.filter(DBTestTable1.name == "name1")
    print fs.count()
# 3
# 2


def t6():
    config()
    test1 = DBTestTable1.find_all()
    print test1.count()
    fs = test1.filter(DBTestTable1.name == "name1",
                      DBTestTable1.description == "description2")
    print fs.count()
# 3
# 1

# 442a0ef0-4c82-45a4-9985-074a6c531e28	2018-11-16 17:33:35	2018-11-16 17:33:35	name2	description1	0
# b9159d4b-43bb-4876-b1df-304cc2d93364	2018-11-16 17:21:25	2018-11-16 17:21:25	name1	description2	0
# e33d0153-ec85-4731-bc87-73f818017dbd	2018-11-16 17:21:51	2018-11-16 17:21:51	name1	description1	0
# e33d0153-ec85-4731-bc87-73f818017dbf	2018-11-17 09:51:54	2018-11-16 09:52:02	name1	description1	1


def t7():
    config()
    filters = [
        DBTestTable1.name == "name1",
        DBTestTable1.description == "description1"
    ]
    test1 = DBTestTable1.find_by_filter(filters=filters)
    print test1.count()

    test2 = DBTestTable1.find_by_filter(filters=filters, id="e33d0153-ec85-4731-bc87-73f818017dbd")
    print test2.count()
# 2
# 1


def t8():
    config()
    test1 = DBTestTable1.get_by(id="e33d0153-ec85-4731-bc87-73f818017dbd")
    print test1.data()
    test2 = DBTestTable1.get_by(id="e33d0153-ec85-4731-bc87-73f818017dbe")
    if test2 is None:
        print "not exist"
    test2 = DBTestTable1.find_by(id="e33d0153-ec85-4731-bc87-73f818017dbe")
    if test2 is None:
        print "not exist"
# {'updated': datetime.datetime(2018, 11, 16, 17, 21, 51), 'description': u'description1',
# 'created': datetime.datetime(2018, 11, 16, 17, 21, 51), 'deleted': 0L, 'deleted_at': None,
# 'id': u'e33d0153-ec85-4731-bc87-73f818017dbd', 'name': u'name1'}
# not exist


if __name__ == '__main__':
    t8()
