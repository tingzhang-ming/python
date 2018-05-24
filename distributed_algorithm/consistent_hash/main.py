from abc import ABCMeta, abstractmethod
from collections import OrderedDict


class Node(object):

    def __init__(self, domain, ip):

        self.domain = domain
        self.ip = ip
        self.data = {}

    def put(self, key, value):
        self.data[key] = value

    def get(self, key):
        return self.data.get(key) if key in self.data else None
#############################################


class Cluster(metaclass=ABCMeta):

    def __init__(self):
        self.nodes = []

    @abstractmethod
    def add_node(self, node):
        pass

    @abstractmethod
    def remove_node(self, node):
        pass

    @abstractmethod
    def get(self, key):
        pass


class NormalHashCluster(Cluster):

    def add_node(self, node):
        self.nodes.append(node)

    def remove_node(self, node):
        for n in self.nodes:
            if n.ip == node.ip or n.domain == node.domain:
                self.nodes.remove(n)
                break

    def get(self, key):
        hv = hash(key)
        index = abs(hv % len(self.nodes))
        return self.nodes[index]


class ConsistencyHashCluster(Cluster):

    vir_nodes = OrderedDict()

    VIR_NODE_COUNT = 512

    SPLIT = "#"

    @staticmethod
    def get_hash(s):
        # p = 16777619
        # hv = 2166136261
        # for ss in s:
        #     hv = (hv ^ ord(ss)) * p
        # hv += hv << 13
        # hv ^= hv >> 7
        # hv += hv >> 17
        # hv += hv << 5
        # return (abs(hv) if hv < 0 else hv) % 2166136261
        return hash(s)

    def add_node(self, node):
        self.nodes.append(node)
        for i in range(self.VIR_NODE_COUNT):
            hv = self.get_hash("%s%s%d" % (node.ip, self.SPLIT, i))
            self.vir_nodes[hv] = node
        self.vir_nodes = OrderedDict(sorted(self.vir_nodes.items(), key=lambda t: t[0]))

    def remove_node(self, node):
        have = False
        for n in self.nodes:
            if n.ip == node.ip or n.domain == node.domain:
                self.nodes.remove(n)
                have = True
                break
        if have is False:
            return
        for i in range(self.VIR_NODE_COUNT):
            hv = self.get_hash("%s%s%d" % (node.ip, self.SPLIT, i))
            del self.vir_nodes[hv]

    def get(self, key):
        hv = self.get_hash(key)
        # print(hv)
        sub_key = [k for k in self.vir_nodes.keys() if k > hv]
        if len(sub_key) == 0:
            sub_key =[k for k in self.vir_nodes.keys()]
        # print(len(sub_key))
        # print(sub_key[0])
        return self.vir_nodes[sub_key[0]]
############################################################


DATA_COUNT = 1000
PRE_KEY = "mhc"


def hit(cluster):
    h = 0
    for i in range(DATA_COUNT):
        if "%s%d" % (PRE_KEY, i) in cluster.get("%s%d" % (PRE_KEY, i)).data:
            h += 1
    a = h/DATA_COUNT
    print("缓存命中率: %f" % a)


def test(cluster):
    cluster.add_node(Node("c1.mhc.info", "192.168.0.1"))
    cluster.add_node(Node("c2.mhc.info", "192.168.0.2"))
    cluster.add_node(Node("c3.mhc.info", "192.168.0.3"))
    cluster.add_node(Node("c4.mhc.info", "192.168.0.4"))

    for i in range(DATA_COUNT):
        node = cluster.get("%s%d" % (PRE_KEY, i))
        node.put("%s%d" % (PRE_KEY, i), "Test Data")

    print("数据分布情况: ")
    for n in cluster.nodes:
        print("IP: %s, 数据量: %d" % (n.ip, len(n.data)))
    hit(cluster)

    print("增加一个节点")
    cluster.add_node(Node("c5.mhc.info", "192.168.0.5"))
    hit(cluster)

    print("去掉一个节点")
    cluster.remove_node(cluster.nodes[0])
    hit(cluster)


def main():
    cluster1 = NormalHashCluster()
    cluster2 = ConsistencyHashCluster()

    print("--------normal hash---------")
    test(cluster1)
    print("--------consistent hash---------")
    test(cluster2)


if __name__ == '__main__':
    main()

# --------normal hash---------
# 数据分布情况:
# IP: 192.168.0.1, 数据量: 226
# IP: 192.168.0.2, 数据量: 259
# IP: 192.168.0.3, 数据量: 248
# IP: 192.168.0.4, 数据量: 267
# 缓存命中率: 1.000000
# 增加一个节点
# 缓存命中率: 0.190000
# 去掉一个节点
# 缓存命中率: 0.000000
# --------consistent hash---------
# 数据分布情况:
# IP: 192.168.0.1, 数据量: 238
# IP: 192.168.0.2, 数据量: 239
# IP: 192.168.0.3, 数据量: 268
# IP: 192.168.0.4, 数据量: 255
# 缓存命中率: 1.000000
# 增加一个节点
# 缓存命中率: 0.811000
# 去掉一个节点
# 缓存命中率: 0.620000
