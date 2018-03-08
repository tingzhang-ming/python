from car import CarModel


class BenzModel(CarModel):

    def start(self):
        print "Benz start"

    def stop(self):
        print "Benz stop"

    def alarm(self):
        print "Benz alarm"
