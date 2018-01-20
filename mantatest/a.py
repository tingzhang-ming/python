import manta as pymanta

manta_pk = "-----BEGIN RSA PRIVATE KEY-----#MIIEowIBAAKCAQEArdxFHj3hv4Ii+cQBu5/K4670JapHts7aBaeNDFin8U58yIE+#d/3/zJd2I5+2m3217HE5FXJD3V+JyLJ4T1m/AY8l1II+2zNqmm/q+QmhBw8rFbJ1#O8y/HuC54LGkq/BGYT+NUtG4Gh6/3JAGHD+TAz4KFUp+pUV+t9VoKx2vPXqPD7xg#iRYCmgt/hIxX+f+tQ4PAIr9hNbsJrm6OMB+eoXV7whY3dC9gfsXrUEHO9NzdLD87#Ffjm1RckLiF8a2ulaKgWVmmUVqb7JcWDPhYMwEaLJGVOw5g3v9+xQrUbY5ObTIy7#C/IlGhAmd6P+hmwSz6OQoNa6KWqnvUekv7am7QIDAQABAoIBAFqS7DcrCdZZF5uC#71wtjOc8l9ifcyjbbl2Pwj1yWluuBff2zPJ6Eq8lINjCNcGfpgz9lz2C/7PuN7uk#rmS4XneTeaPSDqjnilvWflUrHQauckWlaMm0isStUmiqYx1n2WKEVz2UIBMLfeyL#44MH47DGuz4IRx4WrENdHB2KI2ck/DmPG0uPP+eQuI5G4VvNp9bckilHwS76b0RX#cHjF55DxKlP4TPjPDL3k9jRtAw3UxSMsks2xrRtIg0oiF8vEcCXrROaRPgk4FcJf#wuKEchgfOoONcGB1R/7Hye/EDYOjWDbW2O3uZVT/YenLhTXMj3vKMNFN29NErRAb#bLEV1gECgYEA2q4VeMDIo6nPD1GSra8oLFJBpNTpt0Hjqeni9aY2+0CMHi7vChXG#Izrj9RxhRJqKS2F+6p22r1DhMu19Xb0iAZkAZW7ryNcuyaUNsmLsMQPs4VUyhVAQ#k6yMu4Pwb/AFWsxHvOrvS/T+5iP+TBXIzv0YPrxuv5QsGj4/Gq1gdi0CgYEAy4gP#7qz5nwLToQTtGeOOMKJJAyGcijcOnkQc0+/hSZrhogn2kUe06dlpc5r7V7B6G3FF#Z9yf5F7QJNl8poCbhQ0g+V35qLA0ywudybsXd+q1Y+gAoAwtvD+246IUooQXDF93#Abjh87zS0LdcdozglvlETvEWfv2sj/MhVkk0K8ECgYB2MNKgEioe8t9bmy4Yu2uO#EOMz0HOFPZJrumKVfEGJKIjSo3FE1SHi1qhwSOd1acVHGqm66oTbWm5s1RkF+fwQ#Ov6Q1BOR2GOMTq4JdRfNIh78ZszIas6a0g66JoRkK6jpOzGmtJ+jQQYnotqFitye#qwJYngWJe+8eO/hlVcGl/QKBgQC+I+GGfzBAPdrJXZnHis+mXaXJ+BePA/pzHnyz#/jDAm6HYyGgBtzSrFsIuDwZqGGMqyfomGnWBWpYnJssNna4scWRxsjpvPhZD7hk9#gbxd+fX1XKNg4Z/Ect1/8UZHwRDrLTA3eqoUEz37YKFP2zJhuIL5IL98aa5RWLi3#LHJBwQKBgG9PGKQISss7LShb/x/IIAHCWS1Z+mB+V3vG2HhgEQvXJIM1ogRBUCox#i36Eor4ERC5KQj298ERO8LXc9NeL5zDWEam+jhdh7iSaNksmvPRqDOwfu6YkmqTH#Jk+5yAXYQFKcYeHteCgQIt9qPNYXaN6Mbysbj6SFBpKYubKCbTQg#-----END RSA PRIVATE KEY-----#"
private_key = manta_pk.replace('#', '\n')
key_id = "d8:69:9d:07:60:0a:0f:2c:19:59:e0:5e:aa:c7:84:51"
account = "dbba"
url = "https://109.105.30.55"
is_tls = True
signer = pymanta.PrivateKeySigner(key_id, private_key)

client = pymanta.MantaClient(
    url,
    account,
    disable_ssl_certificate_validation=is_tls,
    signer=signer)
bucket = '/{}/stor/dbau'.format(account)

# client.mkdir('{}/multiazjubin'.format(bucket), parents=True)

for i in client.list_directory(bucket):
    print i['name']
