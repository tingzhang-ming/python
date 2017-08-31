import unittest
import random

class Test(unittest.TestCase):

    def setUp(self):
        self.seq = range(10)

    def test_shuffle(self):
        # make sure the shuffled sequence does not lose any elements
        random.shuffle(self.seq)
        self.seq.sort()
        self.assertEqual(self.seq, range(10))

        # should raise an exception for an immutable sequence
        self.assertRaises(TypeError, random.shuffle, (1, 2, 3))

    def test_choice(self):
        element = random.choice(self.seq)
        self.assertTrue(element in self.seq)

    def test_error(self):
        element = random.choice(self.seq)
        self.assertTrue(element not in self.seq)

if __name__ == "__main__":
    unittest.main()

"""

Ran 3 tests in 0.019s

FAILED (failures=1)
 
 

Failure
Traceback (most recent call last):
  File "/usr/lib64/python2.7/unittest/case.py", line 369, in run
    testMethod()
  File "/root/github/python/unittest/a.py", line 24, in test_error
    self.assertTrue(element not in self.seq)
  File "/usr/lib64/python2.7/unittest/case.py", line 462, in assertTrue
    raise self.failureException(msg)
AssertionError: False is not true
"""