import zipfile
from io import BytesIO
import base64
import os
import tempfile

def t1():
    zipoutput = BytesIO()
    zf = zipfile.ZipFile(zipoutput, mode='w')
    args = '{"ANSIBLE_MODULE_ARGS": {"_ansible_version": "2.4.0", "_uses_shell": true, "_ansible_no_log": false, "_ansible_module_name": "command", "_raw_params": "pwd", "_ansible_verbosity": 4, "_ansible_syslog_facility": "LOG_USER", "_ansible_socket": null, "_ansible_selinux_special_fs": ["fuse", "nfs", "vboxsf", "ramfs", "9p"], "_ansible_diff": false, "_ansible_debug": false, "_ansible_check_mode": false}}'
    zf.writestr("ansible_args",args)
    zf.close()
    ZIPDATA = base64.b64encode(zipoutput.getvalue())

    print "========"
    print ZIPDATA

    temp_path = tempfile.mkdtemp(prefix='ansible_')

    zipped_mod = os.path.join(temp_path, 'ansible_modlib.zip')
    modlib = open(zipped_mod, 'wb')
    modlib.write(base64.b64decode(ZIPDATA))
    modlib.close()

    z = zipfile.ZipFile(zipped_mod, mode='r')
    print(z.read('ansible_args'))

if __name__ == '__main__':
    t1()