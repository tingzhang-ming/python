import functools
import json

class JSONOutputError(Exception):

    def __init__(self, message):
        self._message = message

    def __str__(self):
        return self._message

def json_output(decorated):
    @functools.wraps(decorated)
    def inner(*args, **kwargs):
        try:
            result = decorated(*args, **kwargs)
        except JSONOutputError as ex:
            result = {
                'status': 'error',
                'message': str(ex),
            }
        return json.dumps(result)
    return inner

@json_output
def error():
    raise JSONOutputError('This function is erratic.')


if __name__ == '__main__':
    print error()
