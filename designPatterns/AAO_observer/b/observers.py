from observer import Observer


class Lisi(Observer):

    def update(self, observable, context):
        print "li si observe han fei zi"
        print "bao gao: ", context


class Wangsi(Observer):

    def update(self, observable, context):
        print "Wang si observe han fei zi"
        print "Wo kan jian: ", context
