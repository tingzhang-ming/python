import os
import signal
import logging
import subprocess

LOG = logging.getLogger(__name__)


def raise_if_process_errored(process, exception):
    try:
        err = process.stderr.read()
        if err:
            raise exception(err)
    except OSError:
        pass


class BackupError(Exception):
    """Error running the Backup Command."""


class UnknownBackupType(Exception):
    """Unknown backup type."""


class BackupRunner(object):
    """Base class for Backup Strategy implementations."""
    __strategy_type__ = 'backup_runner'
    __strategy_ns__ = 'trove.guestagent.strategies.backup'

    # The actual system call to run the backup
    cmd = None
    is_zipped = False

    def __init__(self, filename, **kwargs):
        self.base_filename = filename
        self.process = None
        self.pid = None
        kwargs.update({'filename': filename})
        self.command = self.cmd % kwargs

    @property
    def backup_type(self):
        return type(self).__name__

    def _run(self):
        LOG.debug("BackupRunner running cmd: %s", self.command)
        self.process = subprocess.Popen(self.command, shell=True,
                                        stdout=subprocess.PIPE,
                                        stderr=subprocess.PIPE,
                                        preexec_fn=os.setsid)
        self.pid = self.process.pid

    def __enter__(self):
        """Start up the process."""
        self._run_pre_backup()
        self._run()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """Clean up everything."""
        if exc_type is not None:
            return False

        if getattr(self, 'process', None):
            try:
                # Send a sigterm to the session leader, so that all
                # child processes are killed and cleaned up on terminate
                # (Ensures zombie processes aren't left around on a FAILURE)
                # https://bugs.launchpad.net/trove/+bug/1253850
                os.killpg(self.process.pid, signal.SIGTERM)
                self.process.terminate()
            except OSError:
                # Already stopped
                pass
            # raise_if_process_errored(self.process, BackupError)
            if not self.check_process():
                raise BackupError

        self._run_post_backup()

        return True

    def metadata(self):
        """Hook for subclasses to store metadata from the backup."""
        return {}

    @property
    def filename(self):
        """Subclasses may overwrite this to declare a format (.tar)."""
        return self.base_filename

    @property
    def manifest(self):
        return "%s%s" % (self.filename,
                         self.zip_manifest)

    @property
    def zip_cmd(self):
        return ' | gzip' if self.is_zipped else ''

    @property
    def zip_manifest(self):
        return '.gz' if self.is_zipped else ''

    def check_process(self):
        """Hook for subclasses to check process for errors."""
        return True

    def read(self, chunk_size):
        return self.process.stdout.read(chunk_size)

    def _run_pre_backup(self):
        pass

    def _run_post_backup(self):
        pass
