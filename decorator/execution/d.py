import functools
import json

def json_output(decorated):
    @functools.wraps(decorated)
    def inner(*args, **kwargs):
        result = decorated(*args, **kwargs)
        return json.dumps(result)
    return inner

@json_output
def do_nothing():
    return {'status':'done'}


if __name__ == '__main__':
    print json.loads(do_nothing())
