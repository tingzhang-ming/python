import redis
import time

if __name__ == "__main__":
    r = redis.StrictRedis(host="localhost", port=6379, db=0)
    pre = r.lastsave()
    #2017-08-30 13:35:55
    print pre
    r.bgsave()
    timeout = 60
    while True:
        now = r.lastsave()
        if now == pre:
            time.sleep(1)
            print "wait"
        else:
            print now
            print "backup succeed"
            break
        timeout -= 1
        if timeout <= 0:
            print "timeout"
            break