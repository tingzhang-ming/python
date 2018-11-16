

def t1():
    kwargs = {"filters": ["haha", "aa"], "2": "2"}
    filters = kwargs.pop('filters', [])
    print filters
    print kwargs
# ['haha', 'aa']
# {'2': '2'}


if __name__ == '__main__':
    t1()
