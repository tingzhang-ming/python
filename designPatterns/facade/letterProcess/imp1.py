from letterProcess import AbstractLetterProcess


class LetterProcessImpl(AbstractLetterProcess):

    def write(self, context):
        print "write:", context

    def fill(self, address):
        print "fill address:", address

    def send(self):
        print "send letter"
