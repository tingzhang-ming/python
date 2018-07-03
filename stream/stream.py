

def stream(it):
    tmp = iter(it)
    while True:
        try:
            yield tmp.next()
        except StopIteration:
            break


def stream_map(func, stream):
    while True:
        yield func(stream.next())


def stream_filter(pred, stream):
    while True:
        x = stream.next()
        if pred(x):
            yield x