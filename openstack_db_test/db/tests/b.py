# encoding: utf-8
import random
from db import get_db_api
from db.data_models.test1 import DBTestTable2

options = dict(
    sql_connection="mysql://root:123@ali:3306/db_test",
    opts={}
)

db_api = get_db_api()


def config():
    db_api.configure_db(options)


def t1():
    config()
    for i in range(2, 50):
        DBTestTable2.create(id=i, name="name-%d" % i, age=random.randint(1, 70))


# limit, marker, marker_column=None
# limit 是显示个数
# marker 是偏移量，但是主键要是数字(marker_column为空时)
def t2():
    config()
    t = DBTestTable2.find_all()
    tt = t.limit(5, 10, marker_column=DBTestTable2.age)

    for i in tt:
        print "id: %d, age: %d" % (i.id, i.age)
# id: 19, age: 11
# id: 8, age: 12
# id: 9, age: 13
# id: 14, age: 17
# id: 20, age: 17


def t3():
    config()
    ts = DBTestTable2.find_all()
    test1 = DBTestTable2.find_by_pagination("test2", ts, "foo", limit=5, marker=0)
    for t in test1.collection:
        print t.id
    print test1.data()
    print test1.next_page_marker
# 1
# 2
# 3
# 4
# 5
# {'total_count': 49L, 'test2': [<db.data_models.test1.DBTestTable2 object at 0x00000000078D5B38>,
# <db.data_models.test1.DBTestTable2 object at 0x00000000078D5BE0>,
# <db.data_models.test1.DBTestTable2 object at 0x00000000078D5C50>,
# <db.data_models.test1.DBTestTable2 object at 0x00000000078D5CC0>,
# <db.data_models.test1.DBTestTable2 object at 0x00000000078D5D30>],
# 'links': [{'href': 'https:///foo?marker=5', 'rel': 'next'}]}


def t4():
    config()
    ts = DBTestTable2.find_all()
    next_marker = 0
    i = 1
    while next_marker is not None:
        data = DBTestTable2.find_by_pagination("test2", ts, "foo", limit=5, marker=next_marker)
        next_marker = data.next_page_marker
        print "page %d:" % i
        print str([d.id for d in data.collection])
        i += 1
# page 1:
# [1L, 2L, 3L, 4L, 5L]
# page 2:
# [6L, 7L, 8L, 9L, 10L]
# page 3:
# [11L, 12L, 13L, 14L, 15L]
# page 4:
# [16L, 17L, 18L, 19L, 20L]
# page 5:
# [21L, 22L, 23L, 24L, 25L]
# page 6:
# [26L, 27L, 28L, 29L, 30L]
# page 7:
# [31L, 32L, 33L, 34L, 35L]
# page 8:
# [36L, 37L, 38L, 39L, 40L]
# page 9:
# [41L, 42L, 43L, 44L, 45L]
# page 10:
# [46L, 47L, 48L, 49L]


def t5():
    config()
    ts = DBTestTable2.find_all()
    next_marker = 0
    i = 1
    while next_marker is not None:
        data = DBTestTable2.find_by_pagination("test2", ts, "foo",
                                               limit=5,
                                               marker=next_marker,
                                               marker_column=DBTestTable2.age)
        next_marker = data.next_page_marker

        print "page %d:" % i
        print str([[d["id"], d.age] for d in data.collection])
        i += 1
# [[3L, 2L], [26L, 3L], [40L, 4L], [46L, 5L], [30L, 7L]]
# page 2:
# [[30L, 7L], [19L, 11L], [8L, 12L], [9L, 13L], [14L, 17L]]
# page 3:
# [[19L, 11L], [8L, 12L], [9L, 13L], [14L, 17L], [35L, 17L]]
# page 4:
# [[20L, 17L], [35L, 17L], [14L, 17L], [1L, 18L], [24L, 19L]]
# page 5:
# [[7L, 21L], [39L, 22L], [25L, 22L], [49L, 23L], [28L, 25L]]
# page 6:
# [[45L, 26L], [34L, 27L], [43L, 32L], [33L, 33L], [4L, 34L]]
# page 7:
# [[43L, 32L], [33L, 33L], [4L, 34L], [5L, 34L], [29L, 39L]]
# page 8:
# [[29L, 39L], [44L, 41L], [47L, 43L], [21L, 45L], [36L, 45L]]
# page 9:
# [[44L, 41L], [47L, 43L], [21L, 45L], [42L, 45L], [36L, 45L]]
# page 10:
# [[18L, 46L], [13L, 46L], [27L, 47L], [16L, 49L], [12L, 50L]]
# page 11:
# [[15L, 51L], [2L, 53L], [10L, 53L], [31L, 53L], [32L, 54L]]
# page 12:
# [[11L, 57L], [23L, 57L], [38L, 59L], [41L, 61L], [48L, 61L]]
# page 13:
# [[41L, 61L], [48L, 61L], [37L, 63L], [17L, 68L]]


def t6():
    config()
    ts = DBTestTable2.find_all()
    next_marker = 0
    i = 1
    while next_marker is not None:
        data = DBTestTable2.find_by_pagination2("test2", ts, "foo",
                                                limit=5,
                                                marker=next_marker,
                                                marker_column=DBTestTable2.age)
        next_marker = data.next_page_marker

        print "page %d:" % i
        print str([[d["id"], d.age] for d in data.collection])
        i += 1


def t7():
    config()
    ts = DBTestTable2.find_all()
    ts2 = ts.filter(DBTestTable2.age < 18)
    ts3 = ts2.order_by(DBTestTable2.age, DBTestTable2.id)
    for d in ts3:
        print d["id"], d.age


if __name__ == '__main__':
    t7()
