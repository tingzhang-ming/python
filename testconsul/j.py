import os
import consul


os.environ['http_proxy'] = ''
c = consul.Consul(host="127.0.0.1")

c.event.fire(name='mhc', service='mysqlms924-mysql-primary')

es = c.event.list('mhc')[1]
for e in es:
    print e
