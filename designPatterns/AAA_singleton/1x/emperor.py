

class Emperor(object):

    def __init__(self):
        self.name = None

    def say(self):
        print("my name: %s" % self.name)

_emperor = Emperor()


def get_instance():
    return _emperor
