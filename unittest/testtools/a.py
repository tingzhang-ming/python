from testtools import TestCase


class TestLearnTesttools(TestCase):

    def setUp(self):
        super(TestLearnTesttools, self).setUp()
        print "this is setUp"

    def test_case_1(self):
        self.assertIn('a', 'cat')

    def test_case_2(self):
        assert 2 == 3

    def tearDown(self):
        super(TestLearnTesttools, self).tearDown()
        print "this is tearDown"

    @classmethod
    def setUpClass(cls):
        print "this is setUp class"

"""
(venv) D:\github\python\unittest\testtools>python -m testtools.run a.py
Tests running...
this is setUp class
this is setUp
this is tearDown
this is setUp
this is tearDown
======================================================================
FAIL: a.TestLearnTesttools.test_case_2
----------------------------------------------------------------------
Traceback (most recent call last):
  File "a.py", line 14, in test_case_2
    assert 2 == 3
AssertionError

Ran 2 tests in 0.002s
FAILED (failures=1)

"""

"""
nosetests a.py
.F
======================================================================
FAIL: a.TestLearnTesttools.test_case_2
----------------------------------------------------------------------
_StringException: Traceback (most recent call last):
  File "D:\github\python\unittest\testtools\a.py", line 14, in test_case_2
    assert 2 == 3
AssertionError

-------------------- >> begin captured stdout << ---------------------
this is setUp
this is tearDown

--------------------- >> end captured stdout << ----------------------

----------------------------------------------------------------------
Ran 2 tests in 0.002s

FAILED (failures=1)

"""