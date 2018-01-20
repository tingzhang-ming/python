import os
import consul


os.environ['http_proxy'] = ''
c = consul.Consul(host="127.0.0.1")

index, data = c.kv.get("mhc", index=108405)
print index
print data


