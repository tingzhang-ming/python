from util import *
import itertools
import urllib2

max_errors = 5
num_errors = 0

for page in itertools.count(1):
    url = base_url + "/view/%d" %page
    html = download(url)
    if html is None:
        num_errors += 1
        if num_errors == max_errors:
            break
    else:
        num_errors = 0
