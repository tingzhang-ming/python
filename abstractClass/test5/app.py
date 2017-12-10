
class App(object):

    def __init__(self, at):
        self.at = at

    def __call__(self, *args, **kwargs):
        self.at.method1(name=kwargs["name"])
