import threading
from time import ctime


class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args
        self.result = None

    def get_result(self):
        return self.result

    def run(self):
        print 'starting', self.name, 'at:', ctime()
        self.result = self.func(*self.args)
        print self.name, 'finished at:', ctime()
