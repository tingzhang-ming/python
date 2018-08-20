from factory import AbstractHumanFactory


class HumanFactory(AbstractHumanFactory):

    def create_human(self, name):
        human_module = __import__("human.{}".format(name), fromlist=["human"])
        return vars(human_module)[name]()
