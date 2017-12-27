import requests


def t1():
    r = requests.get('https://github.com/timeline.json')
    print r.content


if __name__ == '__main__':
    t1()
