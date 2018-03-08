from factory import AbstractHumanFactory


class FemaleFactory(AbstractHumanFactory):

    def create_human(self, name):
        human_module = __import__("human.{}Human".format(name), fromlist=["human"])
        return vars(human_module)["Female{}Human".format(name)]()


class MaleFactory(AbstractHumanFactory):

    def create_human(self, name):
        human_module = __import__("human.{}Human".format(name), fromlist=["human"])
        return vars(human_module)["Male{}Human".format(name)]()
