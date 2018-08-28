from handler import Handler, LEVELS


class Father(Handler):

    def __init__(self):
        super(Father, self).__init__(LEVELS.father)

    def response(self, women):
        print "daughter request father"
        print women.get_request()
        print "father response: agree"


class Husband(Handler):

    def __init__(self):
        super(Husband, self).__init__(LEVELS.husband)

    def response(self, women):
        print "wife request husband"
        print women.get_request()
        print "husband response: agree"


class Son(Handler):

    def __init__(self):
        super(Son, self).__init__(LEVELS.son)

    def response(self, women):
        print "mother request son"
        print women.get_request()
        print "son response: agree"
