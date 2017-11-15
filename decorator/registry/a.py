
registry = []

def register(decorated):
    registry.append(decorated)
    return decorated

@register
def foo():
    return 3

@register
def bar():
    return 5

if __name__ == '__main__':
    answers = []
    for func in registry:
        answers.append(func())
    print answers