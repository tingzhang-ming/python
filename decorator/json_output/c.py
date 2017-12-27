import functools
import json


class JSONOutputError(Exception):
    def __init__(self, message):
        self._message = message

    def __str__(self):
        return self._message


def json_output(decorated_=None, indent=None, sort_keys=False):
    if decorated_ and (indent or sort_keys):
        raise RuntimeError('Unexpected arguments.')

    def actual_decorator(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
            except JSONOutputError as ex:
                result = {
                    'status': 'error',
                    'message': str(ex)
                }
            return json.dumps(result, indent=indent, sort_keys=sort_keys)
        return inner

    if decorated_:
        return actual_decorator(decorated_)
    else:
        return actual_decorator


@json_output
def a():
    raise JSONOutputError('This function is erratic.')


@json_output(indent=2, sort_keys=True)
def b():
    raise JSONOutputError('This function is erratic.')


if __name__ == '__main__':
    print a()
    print b()

# {"status": "error", "message": "This function is erratic."}
# {
#   "message": "This function is erratic.",
#   "status": "error"
# }
