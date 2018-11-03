#encoding: utf-8
import mock
import unittest.unittest.unittest

class Count():

    def add(self, a, b):
        return a + b

class MockDemo(unittest.unittest.TestCase):

    def test_add(self):
        count = Count()
        count.add = mock.Mock(side_effect=count.add)
        result = count.add(8, 8)
        print(result)
        count.add.assert_called_with(8, 8)  #检查mock方法是否获得了正确的参数
        self.assertEqual(result, 16)

if __name__ == '__main__':
    unittest.unittest.main()

"""
16
  

Ran 1 test in 0.001s

OK
"""