

def grep(pattern):
    print 'Looking for %s' % pattern
    while True:
        line = (yield)
        if pattern in line:
            print line


if __name__ == '__main__':
    g = grep('python')
    g.next()
    g.send("Yeah, but no, but ..")
    g.send("A series of tubes")
    g.send("python generators rock")
    g.send("python generators rock222222")
"""
Looking for python
python generators rock
python generators rock222222
"""

