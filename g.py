
class InvalidTime(ValueError):
    """ parse time error """
    pass


def parse_time(timestring):
    """
      Parse a time string to (int) seconds
      raise InvalidTime
    """
    bases = (('d', 86400), ('h', 3600), ('m', 60), ('s', 1))
    timestr = timestring.lower()
    for base, multiplier in bases:
        try:
            timesplit = timestr.split(base)
        except AttributeError:
            raise InvalidTime("%s not a valid time string" % timestring)
        if len(timesplit) > 2:
            raise InvalidTime("%s not a valid time string" %timestring)
        if len(timesplit) == 2:
            if timesplit[1]:
                raise InvalidTime("%s not a valid time string" % timestring)
            try:
                amount = int(timesplit[0]) * multiplier
            except ValueError:
                raise InvalidTime("%s not a valid time string" % timestring)
            else:
                return amount
    raise InvalidTime("%s not a valid time string" % timestring)


def t1():
    a = '1d'
    print parse_time(a)


def t2():
    print 24 * 3600


if __name__ == '__main__':
    t2()
