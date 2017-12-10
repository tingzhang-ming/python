import subprocess
import logging

LOG = logging.getLogger(__name__)

CHUNK_SIZE = 2 ** 4
BACKUP_USE_GZIP = False


class RestoreError(Exception):
    """Error running the Backup Command."""


class RestoreRunner(object):
    """Base class for Restore Strategy implementations."""
    """Restore a database from a previous backup."""

    # The actual system calls to run the restore and prepare
    restore_cmd = None

    # The backup format type
    restore_type = None

    # Decryption Parameters
    is_zipped = BACKUP_USE_GZIP

    base_restore_cmd = 'sudo xbstream -x -C %(restore_location)s'

    def __init__(self, storage, **kwargs):
        self.storage = storage
        self.location = kwargs.pop('location')
        self.checksum = kwargs.pop('checksum')
        self.restore_location = kwargs.get('restore_location')
        self.restore_cmd = (self.unzip_cmd +
                            (self.base_restore_cmd % kwargs))
        super(RestoreRunner, self).__init__()

    def pre_restore(self):
        """Hook that is called before the restore command."""
        pass

    def post_restore(self):
        """Hook that is called after the restore command."""
        pass

    def restore(self):
        self.pre_restore()
        content_length = self._run_restore()
        self.post_restore()
        return content_length

    def _run_restore(self):
        return self._unpack(self.location, self.checksum, self.restore_cmd)

    def _unpack(self, location, checksum, command):
        stream = self.storage.load(location, checksum)
        process = subprocess.Popen(command, shell=True,
                                   stdin=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
        content_length = 0
        for chunk in stream:
            process.stdin.write(chunk)
            content_length += len(chunk)
        process.stdin.close()
        LOG.debug("Restored %s bytes from stream.", content_length)

        return content_length

    @property
    def unzip_cmd(self):
        return 'gzip -d -c | ' if self.is_zipped else ''
