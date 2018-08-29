from command import AbstractCommand


class Command1(AbstractCommand):

    def execute(self):
        self._rg.find()
        self._cg.find()
        self._rg.add()
        self._cg.add()
        self._rg.plan()
        self._cg.plan()


class Command2(AbstractCommand):

    def execute(self):
        self._rg.find()
        self._cg.find()
        self._rg.delete()
        self._cg.delete()
        self._rg.plan()
        self._cg.plan()
