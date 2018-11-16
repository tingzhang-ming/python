from functools import wraps
import json


def format_result(handler):
    def wrapper(decorated):
        @wraps(decorated)
        def inner(*args, **kwargs):
            result = decorated(*args, **kwargs)
            return handler(result)
        return inner
    return wrapper


format_result_to_list = format_result(handler=lambda x: list(x) if isinstance(x, tuple) else [x])
format_result_to_json = format_result(handler=lambda x: json.dumps(x))


# -----------------------------------------------
@format_result(handler=lambda x: list(x) if isinstance(x, tuple) else [x])
def test():
    return 1


@format_result_to_json
def test2():
    return {"a":2}


def t1():
    print test2()


if __name__ == '__main__':
    t1()

