import consul
import json5
import pwd

c = consul.Consul(host="109.105.30.90")

nodes = c.health.service("test-primary")[1]

for node in nodes:
    print json5.dumps(node)