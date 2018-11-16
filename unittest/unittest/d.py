import unittest
from mock import patch, Mock
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

    @patch.object(d_fun, "multiply")
    def test_add_and_multiply1(self, mock_multiply):
        x = 3
        y = 5
        mock_multiply.return_value = 15
        addition, multiple = d_fun.add_and_multiply(x, y)
        mock_multiply.assert_called_once_with(3, 5)

        self.assertEqual(8, addition)
        self.assertEqual(15, multiple)

    @patch("d_fun.multiply")
    @patch("d_fun.multiply2")
    def test_add_and_multiply3(self, mock_multiply2, mock_multiply):
        x = 3
        y = 5
        mock_multiply.return_value = 999
        mock_multiply2.return_value = 111
        self.assertEqual(999, d_fun.multiply(x, y))
        self.assertEqual(111, d_fun.multiply2(x, y))

    @patch("d_fun.multiply")
    @patch("d_fun.add_and_multiply")
    def test_add_and_multiply4(self, mock_add_and_multiply, mock_multiply):
        x = 3
        y = 5
        mock_multiply.return_value = 999
        mock_add_and_multiply.return_value = (1, 2)
        addition, multiple = d_fun.add_and_multiply(x, y)
        self.assertEqual(999, d_fun.multiply(x, y))
        self.assertEqual(2, multiple)

    def test_add_and_multiply5(self):
        x = 3
        y = 5
        mock_multiply = Mock(return_value=999)
        with patch("d_fun.multiply", mock_multiply):
            addition, multiple = d_fun.add_and_multiply(x, y)
            self.assertEqual(999, multiple)
        addition, multiple = d_fun.add_and_multiply(x, y)
        self.assertEqual(10015, multiple)


if __name__ == "__main__":
    unittest.main()

"""
Ran 1 test in 0.001s

OK
"""