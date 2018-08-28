

class Processor(object):

    def __init__(self, handlers):
        self._handlers = handlers

    def process(self, women):
        for handler in self._handlers:
            if handler.handles(women):
                handler.handle_message(women)
                return
        print("no handler to handle")
