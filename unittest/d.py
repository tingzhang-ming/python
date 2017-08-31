import unittest
from mock import patch
import d_fun

class MyTestCase(unittest.TestCase):

    @patch("d_fun.multiply")
    def test_add_and_multiply2(self, mock_multiply):
        x = 3
        y = 5
        mock_multiply.return_value = 15
        addition, multiple = d_fun.add_and_multiply(x, y)
        mock_multiply.assert_called_once_with(3, 5)

        self.assertEqual(8, addition)
        self.assertEqual(15, multiple)


if __name__ == "__main__":
    unittest.main()

"""
Ran 1 test in 0.001s

OK
"""