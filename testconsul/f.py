import os
import consul

os.environ['http_proxy'] = ''
c = consul.Consul(host="127.0.0.1")

services = c.agent.services()
all_service = set()
for service_id, service in services.items():
    all_service.add(service['Service'])
print all_service
