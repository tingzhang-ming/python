import random
import time

def get_id():
    seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    sa = []
    for i in range(8):
        sa.append(random.choice(seed))
    salt = ''.join(sa)
    return salt

def gettime(timestamp):
  return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestamp))

def restructure(old, new):
    for at in vars(old).keys():
        if at in vars(new).keys():
            setattr(new, at, getattr(old, at))