import consul
import time

c = consul.Consul(host="localhost")

s = consul.Consul.Agent.Service(c)

check = consul.Consul.Agent.Check(c)

check.register(name="mhc",check_id="sdc4",service_id="1234",ttl="20s")

s.register(name="mhc",service_id="1234",port=9898,tags=["sdff"], address="109.105.4.65")


while True:
    check.ttl_pass("sdc","haha")
    time.sleep(10)
    print c.health.service("mhc", passing=True)[1]