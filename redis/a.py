import redis

if __name__ == "__main__":
    r = redis.StrictRedis(host="localhost", port=6379, db=0)
    r.set("mhc","sdfdf")
    print r.get("mhc")
    #sdfdf

    r.mset(name1="sdaf", name2="ffff")
    print r.mget("name1","name2")
    #['sdaf', 'ffff']
    print r.mget({"name1":"sdaf", "name2":"ffff"})
    #['ffff', 'sdaf']