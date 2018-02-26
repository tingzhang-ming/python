# -*- coding:utf-8 -*-

import random
import json

from kubernetes import client, config, watch

schedule_name = "tim"
config.load_kube_config(config_file="/root/test/k8s/client_ssl/kubeconfig")
v1 = client.CoreV1Api()


def nodes_available():
    ready_nodes = []
    for n in v1.list_node().items:
        for status in n.status.conditions:
            if status.status == "True" and status.type == "Ready":
                ready_nodes.append(n.metadata.name)
    return ready_nodes


def scheduler(name, node, namespces="default"):
    print "+++++++++++++++++++++++++++++++++" + node
    body = client.V1Binding()
    tagert = client.V1ObjectReference()
    tagert.kind = "Node"
    tagert.apiVersion = "v1"
    tagert.name = node
    meta = client.V1ObjectMeta()
    meta.name = name
    body.target = tagert
    body.metadata = meta
    return v1.create_namespaced_binding(namespces, body)


def main():
    w = watch.Watch()
    for event in w.stream(v1.list_namespaced_pod, "default"):
        if event['object'].status.phase == "Pending" and event['object'].spec.node_name is None:
            try:
                print event['object'].metadata.name
                res = scheduler(event['object'].metadata.name, random.choice(nodes_available()))
            except client.rest.ApiException as e:
               print json.load(e.body)["message"]

if __name__ == '__main__':
    main()
