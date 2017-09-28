import consul
import json5
import pwd

c = consul.Consul(host="localhost")

nodes = c.health.service("test1-mysql")[1]

critical_check = []
critical_service = []

for node in nodes:
    if node["Checks"][1]["Status"] == "critical":
        critical_check.append(node["Checks"][1]["CheckID"])
        critical_service.append(node["Service"]["ID"])

print critical_service
print critical_check

# for check in checks:
#     print "------------------------"
#     print checks

# print json5.dumps(checks)

# ids = [check["Service"]["ID"] for check in checks]

# print ids