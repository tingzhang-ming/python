import os
import consul


os.environ['http_proxy'] = ''
c = consul.Consul(host="127.0.0.1")

metadata_keys = c.kv.get("mysqlpxc582/metadata", keys=True)[1]

if metadata_keys is not None:
    for metadata_key in metadata_keys:
        print metadata_key, ":", c.kv.get(metadata_key)[1]['Value']

