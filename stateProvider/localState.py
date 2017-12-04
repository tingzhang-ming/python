""" Persist data in local """
import os
import shutil
import errno
from os.path import join, isfile, isdir
try:
    import cPickle as pickle
except ImportError:
    import pickle


def safe_mkdir(directory, clean=False):
    """
        Ensure a directory is present.  If it's not there, create it.  If it is,
        no-op. If clean is True, ensure the directory is empty.
    """
    if clean:
        safe_rmtree(directory)
    try:
        os.makedirs(directory)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise


def safe_rmtree(directory):
    """
        Delete a directory if it's present. If it's not present, no-op.
    """
    if os.path.exists(directory):
        shutil.rmtree(directory, True)


class InvalidLockError(Exception):
    """ invalid lock error: lock is a file, should be directory"""
    pass


class LocalState(object):
    """
    Persist data in local or use local lock
    """
    STATE_DIR = "state"
    LOCK_DIR = "locks"

    def __init__(self, work_dir="/tmp/local_state"):
        self.dir = work_dir
        self.state_dir = join(self.dir, self.STATE_DIR)
        self.lock_dir = join(self.dir, self.LOCK_DIR)
        safe_mkdir(self.state_dir)
        safe_mkdir(self.lock_dir)

    @staticmethod
    def _check_lock(path):
        """ check lock whether is valid """
        if isfile(path):
            raise InvalidLockError()

    def put(self, key, value):
        """ put data to key """
        key_file = join(self.state_dir, key)
        with open(key_file, 'wb') as f:
            pickle.dump(value, f)

    def get(self, key):
        """ get data from key """
        key_file = join(self.state_dir, key)
        if not isfile(key_file):
            return None
        with open(key_file, 'rb') as f:
            return pickle.load(f)

    def remove(self, key):
        """ remove a key """
        key_file = join(self.state_dir, key)
        if not isfile(key_file):
            return True
        try:
            os.remove(key_file)
        except OSError:
            return False
        return True

    def lock(self, key):
        """ lock a key """
        key_dir = join(self.lock_dir, key)
        self._check_lock(key_dir)
        try:
            os.mkdir(key_dir, 0700)
        except OSError:
            return False
        return True

    def is_lock(self, key):
        """ return whether a key is lock """
        key_dir = join(self.lock_dir, key)
        self._check_lock(key_dir)
        if isdir(key_dir):
            return True
        return False

    def unlock(self, key):
        """ unlock a key """
        key_dir = join(self.lock_dir, key)
        self._check_lock(key_dir)
        if isdir(key_dir):
            os.rmdir(key_dir)

    def clear_all(self):
        """ clear all key """
        safe_mkdir(self.lock_dir, clean=True)
        safe_mkdir(self.state_dir, clean=True)
