from hanma import HummerModel


class HummerH1Model(HummerModel):

    def start(self):
        print "h1 start"

    def stop(self):
        print "h1 stop"

    def alarm(self):
        print "h1 alarm"
