import abc
import logging
import six
from oslo_utils import importutils


LOG = logging.getLogger(__name__)
import_class = importutils.import_class
LOG.setLevel(10)


@six.add_metaclass(abc.ABCMeta)
class Strategy(object):

    __strategy_ns__ = None

    __strategy_name__ = None
    __strategy_type__ = None

    def __init__(self):
        self.name = self.get_canonical_name()
        LOG.debug("Loaded strategy %s", self.name)

    def is_enabled(self):
        """
        Is this Strategy enabled?

        :retval: Boolean
        """
        return True

    @classmethod
    def get_strategy(cls, name, ns=None):
        """
        Load a strategy from namespace
        """
        ns = ns or cls.__strategy_ns__
        if ns is None:
            raise RuntimeError('No namespace provided and __strategy_ns__ unset')

        LOG.debug('Looking for strategy %s in %s', name, ns)
        return import_class(ns + "." + name)

    @classmethod
    def get_canonical_name(cls):
        """
        Return the strategy name
        """
        type_ = cls.get_strategy_type()
        name = cls.get_strategy_name()
        return "%s:%s" % (type_, name)

    @classmethod
    def get_strategy_name(cls):
        return cls.__strategy_name__

    @classmethod
    def get_strategy_type(cls):
        return cls.__strategy_type__
