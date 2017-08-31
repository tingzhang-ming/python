import unittest
from mock import MagicMock

m = MagicMock()

m.a.return_value = "haha"

print m.a()

#haha

m.a.side_effect = KeyError("eeee")

m.a()

"""
Traceback (most recent call last):
  File "/root/github/python/unittest/f.py", line 14, in <module>
    m.a()
  File "/usr/lib/python2.7/site-packages/mock/mock.py", line 1062, in __call__
    return _mock_self._mock_call(*args, **kwargs)
  File "/usr/lib/python2.7/site-packages/mock/mock.py", line 1118, in _mock_call
    raise effect
KeyError: 'eeee'
"""