import redis
import time
import subprocess

def start_redis():
    subprocess.check_call("redis-server --appendonly no --protected-mode no --dir /redis/data --daemonize yes", shell=True)

if __name__ == "__main__":
    r = redis.StrictRedis(host="localhost", port=6379)
    subprocess.check_call("redis-server --appendonly no --protected-mode no --dir /redis/data --daemonize yes",
                          shell=True)
    while True:
        try:
            if r.ping():
                break
        except redis.ConnectionError:
            pass
        time.sleep(0.1)
    print r.config_set("appendonly","yes")
    timeout = 600
    while True:
        if r.info()["aof_rewrite_in_progress"] == 0:
            print "done"
            break
        else:
            print "wait"
            time.sleep(0.1)
        timeout -= 1
        if timeout <= 0:
            print "timeout"
            break
    r.shutdown()
