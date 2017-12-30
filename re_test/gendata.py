from random import randrange, choice
from string import ascii_lowercase as lc
from time import ctime, time

tlds = ('com', 'edu', 'net', 'org', 'govp')

for i in xrange(randrange(5, 11)):
    dtint = randrange(int(time()))
    dtstr = ctime(dtint)
    llen = randrange(4, 8)
    login = ''.join(choice(lc) for j in range(llen))
    dlen = randrange(llen, 13)
    dom = ''.join(choice(lc) for j in xrange(dlen))
    print '%s::%s@%s.%s::%d-%d-%d' % (
        dtstr, login, dom, choice(tlds), dtint, llen, dlen
    )

# Sun Nov 29 22:04:41 1970::rylaz@qrliz.edu::28735481-5-5
# Tue Oct 30 19:47:35 2007::utvijg@uusdvdbhoa.net::1193744855-6-10
# Mon Oct  1 08:10:04 1973::imgjkmw@zajbfvfaotc.com::118282204-7-11
# Mon Sep  2 10:42:22 2013::hgsrbmk@mgrdwcyrrrf.org::1378089742-7-11
# Wed Jun 16 00:55:11 1993::jwsl@swecnplr.govp::740163311-4-8
# Fri Mar 22 20:07:57 1996::qpmqhv@zibgkckaib.edu::827496477-6-10
# Thu Nov  6 13:41:53 1986::bwpp@joliztfo.net::531639713-4-8
# Sun Apr  9 02:21:05 1989::ykimegr@kbttzidcoaxr.edu::608062865-7-12
