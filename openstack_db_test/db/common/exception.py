import re
import logging
from db.common.i18n import _
from db.common.base_exception import OpenstackException, DatabaseMigrationError

LOG = logging.getLogger(__name__)


DatabaseMigrationError = DatabaseMigrationError


def safe_fmt_string(text):
    return re.sub(r'%([0-9]+)', r'\1', text)


class TroveError(OpenstackException):
    """Base exception that all custom trove app exceptions inherit from."""
    internal_message = None

    def __init__(self, message=None, **kwargs):
        if message is not None:
            self.message = message
        if self.internal_message is not None:
            try:
                LOG.error(safe_fmt_string(self.internal_message), kwargs)
            except Exception:
                LOG.error(self.internal_message)
        self.message = safe_fmt_string(self.message)
        super(TroveError, self).__init__(**kwargs)


class NotFound(TroveError):

    message = _("Resource %(uuid)s cannot be found.")


class InvalidModelError(TroveError):

    message = _("The following values are invalid: %(errors)s.")


class ModelNotFoundError(NotFound):

    message = _("Not Found.")


class DBConstraintError(TroveError):

    message = _("Failed to save %(model_name)s because: %(error)s.")