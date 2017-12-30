from atexit import register
from re import compile
from threading import Thread
from time import ctime
from urllib2 import urlopen as uopen

REGEX = compile('#([\d,]+) in Books ')
AMZN = 'http://amazon.com/dp/'
ISBNs = {
    '0132269937': 'Core Python Programming',
    '0132356139': 'Python Web Development with Django',
    '0137143419': 'Python Fundamentals',
}


def get_ranking(isbn):
    page = uopen('%s%s' % (AMZN, isbn))
    data = page.read()
    page.close()
    return REGEX.findall(data)[0]


def _show_ranking(isbn):
    print '- %r ranked %s' % (ISBNs[isbn], get_ranking(isbn))


def _main():
    print 'At', ctime(), 'on Amazon...'
    for isbn in ISBNs:
        Thread(target=_show_ranking, args=(isbn,)).start()


@register
def _atexit():
    print 'all DONE at:', ctime()


if __name__ == '__main__':
    _main()
# At Thu Dec 28 13:12:45 2017 on Amazon...
# - 'Core Python Programming' ranked 226,457
# - 'Python Fundamentals' ranked 4,235,911
# - 'Python Web Development with Django' ranked 1,221,275
# all DONE at: Thu Dec 28 13:13:03 2017
