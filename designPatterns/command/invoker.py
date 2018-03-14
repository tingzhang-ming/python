

class Invoker(object):

    def __init__(self):
        self._command = None

    def set_command(self, command):
        self._command = command

    def action(self):
        print "start action--------------"
        self._command.execute()
