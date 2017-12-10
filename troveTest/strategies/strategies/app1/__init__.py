import logging
from strategies.strategy import Strategy

LOG = logging.getLogger(__name__)


def get_app1_strategy(name, ns=__name__):
    LOG.debug("Getting storage strategy: %s.", name)
    return Strategy.get_strategy(name, ns)
