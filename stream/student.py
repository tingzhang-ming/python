# encoding: utf-8
from stream import *


class Student:

    def __init__(self, id, name, age, gradle, major, school):
        self. id = id
        self.name = name
        self.age = age
        self.gradle = gradle
        self.major = major
        self.school = school


def get_students():
    return [
        Student(20160001, "孔明", 20, 1, "土木工程", "武汉大学"),
        Student(20160002, "伯约", 21, 2, "信息安全", "武汉大学"),
        Student(20160003, "玄德", 22, 3, "经济管理", "武汉大学"),
        Student(20160004, "云长", 21, 2, "信息安全", "武汉大学"),
        Student(20161001, "翼德", 21, 2, "机械与自动化", "华中科技大学"),
        Student(20161002, "元直", 23, 4, "土木工程", "华中科技大学"),
        Student(20161003, "奉孝", 23, 4, "计算机科学", "华中科技大学"),
        Student(20162001, "仲谋", 22, 3, "土木工程", "浙江大学"),
        Student(20162002, "鲁肃", 23, 4, "计算机科学", "浙江大学"),
        Student(20163001, "丁奉", 24, 5, "土木工程", "南京大学"),
    ]


def print_name(s):
    for ss in s:
        print ss.name


def t1():
    students = get_students()
    print_name([ss for ss in students if ss.school == "武汉大学"])
    print "============="
    s = stream(students)
    print_name(stream_filter(lambda it: it.school == "武汉大学", s))
# 孔明
# 伯约
# 玄德
# 云长
# =============
# 孔明
# 伯约
# 玄德
# 云长


if __name__ == '__main__':
    t1()
