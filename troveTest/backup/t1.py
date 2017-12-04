from os.path import join
from test import MockBackup
import manta as pymanta
from stream import MantaStorage
import subprocess
import os

def t1():
    with MockBackup(filename="filename",
                          user="user",
                          password="password") as runner:
        print runner.manifest
        while True:
            text = runner.read(2 ** 16)
            if not text:
                break
            else:
                print "----------------------------"
                print text


def get_manta_client():
    manta_pk = "-----BEGIN RSA PRIVATE KEY-----#MIIEowIBAAKCAQEArdxFHj3hv4Ii+cQBu5/K4670JapHts7aBaeNDFin8U58yIE+#d/3/zJd2I5+2m3217HE5FXJD3V+JyLJ4T1m/AY8l1II+2zNqmm/q+QmhBw8rFbJ1#O8y/HuC54LGkq/BGYT+NUtG4Gh6/3JAGHD+TAz4KFUp+pUV+t9VoKx2vPXqPD7xg#iRYCmgt/hIxX+f+tQ4PAIr9hNbsJrm6OMB+eoXV7whY3dC9gfsXrUEHO9NzdLD87#Ffjm1RckLiF8a2ulaKgWVmmUVqb7JcWDPhYMwEaLJGVOw5g3v9+xQrUbY5ObTIy7#C/IlGhAmd6P+hmwSz6OQoNa6KWqnvUekv7am7QIDAQABAoIBAFqS7DcrCdZZF5uC#71wtjOc8l9ifcyjbbl2Pwj1yWluuBff2zPJ6Eq8lINjCNcGfpgz9lz2C/7PuN7uk#rmS4XneTeaPSDqjnilvWflUrHQauckWlaMm0isStUmiqYx1n2WKEVz2UIBMLfeyL#44MH47DGuz4IRx4WrENdHB2KI2ck/DmPG0uPP+eQuI5G4VvNp9bckilHwS76b0RX#cHjF55DxKlP4TPjPDL3k9jRtAw3UxSMsks2xrRtIg0oiF8vEcCXrROaRPgk4FcJf#wuKEchgfOoONcGB1R/7Hye/EDYOjWDbW2O3uZVT/YenLhTXMj3vKMNFN29NErRAb#bLEV1gECgYEA2q4VeMDIo6nPD1GSra8oLFJBpNTpt0Hjqeni9aY2+0CMHi7vChXG#Izrj9RxhRJqKS2F+6p22r1DhMu19Xb0iAZkAZW7ryNcuyaUNsmLsMQPs4VUyhVAQ#k6yMu4Pwb/AFWsxHvOrvS/T+5iP+TBXIzv0YPrxuv5QsGj4/Gq1gdi0CgYEAy4gP#7qz5nwLToQTtGeOOMKJJAyGcijcOnkQc0+/hSZrhogn2kUe06dlpc5r7V7B6G3FF#Z9yf5F7QJNl8poCbhQ0g+V35qLA0ywudybsXd+q1Y+gAoAwtvD+246IUooQXDF93#Abjh87zS0LdcdozglvlETvEWfv2sj/MhVkk0K8ECgYB2MNKgEioe8t9bmy4Yu2uO#EOMz0HOFPZJrumKVfEGJKIjSo3FE1SHi1qhwSOd1acVHGqm66oTbWm5s1RkF+fwQ#Ov6Q1BOR2GOMTq4JdRfNIh78ZszIas6a0g66JoRkK6jpOzGmtJ+jQQYnotqFitye#qwJYngWJe+8eO/hlVcGl/QKBgQC+I+GGfzBAPdrJXZnHis+mXaXJ+BePA/pzHnyz#/jDAm6HYyGgBtzSrFsIuDwZqGGMqyfomGnWBWpYnJssNna4scWRxsjpvPhZD7hk9#gbxd+fX1XKNg4Z/Ect1/8UZHwRDrLTA3eqoUEz37YKFP2zJhuIL5IL98aa5RWLi3#LHJBwQKBgG9PGKQISss7LShb/x/IIAHCWS1Z+mB+V3vG2HhgEQvXJIM1ogRBUCox#i36Eor4ERC5KQj298ERO8LXc9NeL5zDWEam+jhdh7iSaNksmvPRqDOwfu6YkmqTH#Jk+5yAXYQFKcYeHteCgQIt9qPNYXaN6Mbysbj6SFBpKYubKCbTQg#-----END RSA PRIVATE KEY-----#"
    private_key = manta_pk.replace('#', '\n')
    key_id = "d8:69:9d:07:60:0a:0f:2c:19:59:e0:5e:aa:c7:84:51"
    account = "dbba"
    url = "https://109.105.30.55"
    is_tls = True
    signer = pymanta.PrivateKeySigner(key_id, private_key)

    client = MantaStorage(
        url,
        account,
        disable_ssl_certificate_validation=is_tls,
        signer=signer)
    return client


def list():
    print "list---------------------------------------------"
    client = get_manta_client()
    bucket = '/{}/stor/{}'.format(client.account, "test1")
    ls = client.list_directory(join(bucket, 'backups', 'test3-mysql-backup-2017-12-03T07-03-09Z'))
    for l in ls:
        print l


def delete():
    client = get_manta_client()
    bucket = '/{}/stor/{}'.format(client.account, "mhc")
    ls = client.list_directory(join(bucket, "test2"))
    for l in ls:
        client.delete_object(join(bucket, "test2", l['name']))


def get():
    client = get_manta_client()
    bucket = '/{}/stor/{}'.format(client.account, "mhc")
    t2 = join(bucket, "test2")
    fs = client.list_directory(t2)
    for f in fs:
        print client.get_object(join(t2, f['name']))


def get2():
    client = get_manta_client()
    bucket = '/{}/stor/{}'.format(client.account, "mhc")
    t2 = join(bucket, "test2")
    fs = client.list_directory(t2)
    for f in fs:
        res = client.get_object(join(t2, f['name']))
        with open(join("./backs", f['name']), 'w') as fi:
            fi.write(res)


def t2():
    client = get_manta_client()
    bucket = '/{}/stor/{}'.format(client.account, "mhc")
    client.mkdir(bucket)
    print client.list_directory(bucket)
    with MockBackup(filename="filename",
                          user="user",
                          password="password") as runner:
        client.put_object(join(bucket, "test2"), file=runner)
    print client.list_directory(bucket)


def t3():
    client = get_manta_client()
    bucket = '/{}/stor/{}'.format(client.account, "mhc")
    t2 = join(bucket, "test2")
    fs = client.list_directory(t2)
    names = [f['name'] for f in fs]
    names.sort()
    cmd = 'xbstream -x -C /dbnode/data'
    process = subprocess.Popen(cmd, shell=True,
                               stdin=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    for name in names:
        res = client.get_object(join(t2, name))
        process.stdin.write(res)
    process.stdin.close()



if __name__ == '__main__':
    # t2()
    list()
#    delete()
#     get2()
#     t3()
