from copy import copy, deepcopy


class Mail(object):
    
    def __init__(self, adv_template):
        self._context = adv_template.get_adv_context()
        self._subject = adv_template.get_adv_subject()
        self._receiver = None
        self._appellation = None

    def copy(self):
        return copy(self)

    def deep_copy(self):
        return deepcopy(self)

    def set_appellation(self, t):
        self._appellation = t

    def get_appellation(self):
        return self._appellation

    def set_receiver(self, t):
        self._receiver = t

    def get_receiver(self):
        return self._receiver

    def get_subject(self):
        return self._subject
