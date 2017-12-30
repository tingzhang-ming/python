import re


def t1():
    data = 'Sun Nov 29 22:04:41 1970::rylaz@qrliz.edu::28735481-5-5'
    patt = '.+?(\d+-\d+-\d+)'
    res = re.search(patt, data)
    if res:
        print res.group()
        print res.groups()
"""
Sun Nov 29 22:04:41 1970::rylaz@qrliz.edu::28735481-5-5
('28735481-5-5',)
"""


if __name__ == '__main__':
    t1()
