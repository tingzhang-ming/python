import logging
import os
import sys
from functools import wraps

log = logging.getLogger('WORKER')

formatter = logging.Formatter('%(levelname)s: - %(message)s')
console = logging.StreamHandler(sys.stdout)
log.setLevel(logging.getLevelName(
    os.environ.get('WORKER_LOG_LEVEL', 'DEBUG')))
console.setFormatter(formatter)
log.addHandler(console)



def debug(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        name = fn.__name__
        log.info(name)
        log.debug('%s start', name)
        out = apply(fn, args, kwargs)
        log.debug('%s end: ', name)
        return out
    return wrapper


@debug
def a():
    return "ha"


if __name__ == '__main__':
    a()
