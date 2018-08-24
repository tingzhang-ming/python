from hanma import HummerModel


class HummerH2Model(HummerModel):

    def start(self):
        print "h2 start"

    def stop(self):
        print "h2 stop"

    def alarm(self):
        print "h2 alarm"
