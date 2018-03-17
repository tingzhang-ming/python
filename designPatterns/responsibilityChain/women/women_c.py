from women import AbstractWomen
from handler import  LEVELS


class Women(AbstractWomen):

    def __init__(self, type, request):
        self._type = type
        self._request = ""
        if self._type == LEVELS.father:
            self._request = "daughter's request is {}".format(request)
        elif self._type == LEVELS.husband:
            self._request = "wife's request is {}".format(request)
        elif self._type == LEVELS.son:
            self._request = "mother's request is {}".format(request)

    def get_type(self):
        return self._type

    def get_request(self):
        return self._request
