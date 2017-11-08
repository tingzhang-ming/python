import consul
import json5
import pwd

c = consul.Consul(host="127.0.0.1")

s = c.kv.get("test1/cluster/scalings")[1]['Value']

d = json5.loads(s)

node_number = int(d['mysql'])

print node_number