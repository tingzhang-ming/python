from weakref import WeakKeyDictionary


class Descriptor(object):

    def __init__(self, default=''):
        self.default = default
        self.data = WeakKeyDictionary()

    def __get__(self, instance, owner):
        return self.data.get(instance, self.default)

    def __set__(self, instance, value):
        self.data[instance] = value


class SignInfo(object):

    id = Descriptor()
    location = Descriptor()
    subject = Descriptor()
    post_address = Descriptor()

    def __init__(self):
        self.id = ''
        self.location = ''
        self.subject = ''
        self.post_address = ''


class SignInfo4Pool(SignInfo):

    key = Descriptor()

    def __init__(self, key):
        super(SignInfo4Pool, self).__init__()
        self.key = key


class SignInfoFactory(object):

    _pool = {}

    @classmethod
    def get_sign_info(cls, key):
        if key not in cls._pool:
            cls._pool[key] = SignInfo4Pool(key)
            print "put key", key
        else:
            print "get in pool"
        return cls._pool[key]


def main():
    for i in range(4):
        subject = "subject-{}".format(str(i))
        for j in range(30):
            key = '{}-location-{}'.format(subject, str(j))
            SignInfoFactory.get_sign_info(key)
    sign_info = SignInfoFactory.get_sign_info('subject-1-location-1')


if __name__ == '__main__':
    main()
