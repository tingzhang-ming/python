from letterProcess.imp1 import LetterProcessImpl


class ModenPostOffice(object):

    def __init__(self):
        self._lp = LetterProcessImpl()

    def send_letter(self, context, address):
        self._lp.write(context)
        self._lp.fill(address)
        self._lp.send()
