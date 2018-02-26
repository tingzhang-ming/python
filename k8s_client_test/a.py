""" pip install auth """
import sys
from kubernetes import client, config

config.load_kube_config(config_file="/root/test/k8s/client_ssl/kubeconfig")

v1 = client.CoreV1Api()


def list_public_attr(ob):
    for i in dir(ob):
        if i.startswith("_"):
            continue
        print i
    sys.exit(0)


def t1():
    print("Listing pods with their IPs:")
    ret = v1.list_pod_for_all_namespaces(watch=False)
    for i in ret.items:
        print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))


def t11():
    print("Listing pods with their IPs in default namespace:")
    ret = v1.list_namespaced_pod("default")
    for i in ret.items:
        print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))


def t2():
    """
    node attr:
    api_version
    attribute_map
    discriminator
    kind
    metadata
    spec
    status
    swagger_types
    to_dict
    to_str
    """
    print "Listing nodes:"
    ret = v1.list_node()
    for i in ret.items:
        print i.status.addresses[0].address
        for status in i.status.conditions:
            print "status type: %s,  status: %s" %(status.type, status.status)
# Listing nodes:
# 109.105.4.65
# status type: OutOfDisk,  status: False
# status type: MemoryPressure,  status: False
# status type: DiskPressure,  status: False
# status type: Ready,  status: True


if __name__ == '__main__':
    t11()

