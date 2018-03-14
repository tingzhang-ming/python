from abc import ABCMeta, abstractmethod
from group.requirement import RequirementGroup
from group.code import CodeGroup


class AbstractCommand(object):

    __metaclass__ = ABCMeta

    def __init__(self):
        self._rg = RequirementGroup()
        self._cg = CodeGroup()

    @abstractmethod
    def execute(self):
        pass
