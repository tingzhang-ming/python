import redis

if __name__ == "__main__":
    r = redis.StrictRedis(host="109.105.1.254", port=18502, db=0)
    r.set("mhc","sdfdf")
    print r.get("mhc")
    #sdfdf

    r.mset(name1="sdaf", name2="ffff")
    print r.mget("name1","name2")
    #['sdaf', 'ffff']
    print r.mget({"name1":"sdaf", "name2":"ffff"})
    #['ffff', 'sdaf']

    print r.info()["role"]

    print r.ping()

    print r.info().keys()
