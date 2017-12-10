from base import BackupRunner


def create_fake_data():
    from random import choice
    from string import ascii_letters
    res = ''.join([choice(ascii_letters) for _ in range(1024)])
    print res
    return res


class MockBackup(BackupRunner):
    """Create a large temporary file to 'backup' with subprocess."""

    backup_type = 'mock_backup'

    def __init__(self, *args, **kwargs):
        self.data = create_fake_data()
        self.cmd = 'innobackupex --stream=xbstream --user=root --password=root.123 /dbnode/data'
        super(MockBackup, self).__init__(*args, **kwargs)

    def cmd(self):
        return self.cmd
