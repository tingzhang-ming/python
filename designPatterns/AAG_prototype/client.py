from random import randint
from advTemplate import AdvTemplate
from mail import Mail


MAX_COUNT = 6


def send_mail(mail):
    print "title:", mail.get_subject(), "receiver: ", mail.get_receiver(), "...send successfully!"


def get_rand_string(length):
    s = 'abcdefghhigklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    l = len(s)
    res = []
    for _ in range(length):
        res.append(s[randint(0, l-1)])
    return "".join(res)


def main():
    mail = Mail(AdvTemplate())
    for _ in range(MAX_COUNT):
        mail_copy = mail.copy()
        mail_copy.set_appellation("Mr. {}".format(get_rand_string(5)))
        mail_copy.set_receiver("{}@{}.com".format(get_rand_string(5), get_rand_string(8)))
        send_mail(mail_copy)


if __name__ == '__main__':
    main()
