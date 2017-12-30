import re


dat_file = '/root/github/python/pxc/grastate.dat'

with open(dat_file, 'r') as f:
    text = f.read()

re_obj = re.compile('(?m) *safe_to_bootstrap: *0')

if re_obj.search(text) is not None:
    print 'mo'
    new_text = re_obj.sub('safe_to_bootstrap: 1', text)

    with open(dat_file, 'w') as f:
        f.write(new_text)
