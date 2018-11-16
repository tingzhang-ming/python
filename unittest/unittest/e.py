import unittest
from mock import MagicMock

import e_class


class MyTest(unittest.TestCase):

    def test_should_mock_get_10_times_value_with_MagicMock(self):
        p = e_class.Person()
        p.get_10_times_value = MagicMock(return_value=100)

        self.assertEqual(p.get_10_times_value(), 100)

"""
Ran 1 test in 0.001s

OK
"""