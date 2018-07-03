#!/usr/bin/env python
# coding=utf-8
import time


def t1():
    import compute
    compute_test(compute)
# runing1 time: 0.320000 s
# runing2 time: 1.150000 s


def t2():
    import compute1
    compute_test(compute1)
# runing1 time: 0.240000 s
# runing2 time: 0.800000 s


def t3():
    import compute2
    compute_test(compute2)
# runing1 time: 0.000000 s
# runing2 time: 0.720000 s


def t4():
    import compute3
    compute_test(compute3)
# runing1 time: 0.010000 s
# runing2 time: 0.180000 s


def compute_test(compute):
    lon1, lat1, lon2, lat2 = -72.345, 34.323, -61.823, 54.826

    start_time = time.clock()
    compute.f_compute(3.2, 6.9, 1000000)
    end_time = time.clock()
    print "runing1 time: %f s" % (end_time - start_time)
    start_time = time.clock()
    for i in range(1000000):
        compute.spherical_distance(lon1, lat1, lon2, lat2)
    end_time = time.clock()
    print "runing2 time: %f s" % (end_time - start_time)

if __name__ == '__main__':
    t4()

