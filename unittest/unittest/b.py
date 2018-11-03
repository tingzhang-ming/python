import mock
import unittest.unittest.unittest

class Count():

    def add(self):
        pass

# test Count class
class TestCount(unittest.unittest.TestCase):

    def test_add(self):
        count = Count()
        count.add = mock.Mock(return_value=13)
        result = count.add(8,5)
        self.assertEqual(result,13)


if __name__ == '__main__':
    unittest.unittest.main()

"""
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
"""