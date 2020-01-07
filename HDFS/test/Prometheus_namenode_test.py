#!-*- coding:utf-8 -*-

from prometheus_client import start_http_server, Gauge, Counter, Enum, CollectorRegistry
import random
import requests

url = 'http://bdp102.qa.sa.cn:50070/jmx'


class hdfsExporter():
    def __init__(self, url):
        self.url = url

    def get_nnHeap_utilization(self):
        request = requests.get(self.url)
        data = request.json()['beans'][0]
        memmax = data['MemHeapMaxM']
        memused = data['MemHeapUsedM']
        utilization = memused / memmax
        return '%.2f' % utilization

    def get_dfs_utilization(self):
        request = requests.get(self.url)
        data = request.json()['beans'][8]
        capacityUsedGB = data['CapacityUsedGB']
        capacityTotalGB = data['CapacityTotalGB']
        utilization = capacityUsedGB / capacityTotalGB
        return '%.4f' % utilization

    def get_dfs_corruptedRep(self):
        request = requests.get(self.url)
        data = request.json()['beans'][8]
        corrBlock = data['CorruptBlocks']
        return corrBlock

    def get_nn_rpcConn(self):
        request = requests.get(self.url)
        data = request.json()['beans'][37]
        rpcConnNum = data['NumOpenConnections']
        return rpcConnNum

    def get_dfs_totalFiles(self):
        request = requests.get(self.url)
        data = request.json()['beans'][8]
        totalFiles = data['TotalFiles']
        return totalFiles

    def get_dfs_totalBlocks(self):
        request = requests.get(self.url)
        data = request.json()['beans'][8]
        totalBlocks = data['BlocksTotal']
        return totalBlocks

    def get_numAliveNodes(self):
        request = requests.get(self.url)
        data = request.json()['beans'][32]
        numNodes = data['NumLiveDataNodes']
        return numNodes

    def export_Gauge(self):
        # registry = CollectorRegistry()
        g = Gauge('g', 'Description of gauge', ['labelname'])
        g.labels('numAliveNodes').set(random.random())
        return g


'''
print(get_nnHeap_utilization(url))
print(get_dfs_utilization(url))
print(get_nn_rpcConn(url))
print(get_dfs_totalFiles(url))
print(get_dfs_totalBlocks(url))
print(get_numAliveNodes(url))
'''
regis = CollectorRegistry(auto_describe=False)
a = Gauge('namenode', 'Descriptionofgauge', ['cluster', 'service', 'metric'])
b = Gauge('dfsblockscorrupt', 'Corrupted Block Number', ['cluster', 'service', 'metric'])
c = Gauge('dfsNumNodes', 'Alive Nodes', ['cluster', 'service', 'metric'])

e = Enum('my_task_state', 'Description of enum',
         states=['starting', 'running', 'stopped'])

start_http_server(8000)

while True:
    # a.labels(cluster='bdp',service='bdp102',metric='heapuse').set(get_nnHeap_utilization(url))
    # b.labels(cluster='bdp',service='hdfs',metric='repblock').set(get_dfs_corruptedRep(url))
    # c.labels(cluster='bdp',service='hdfs',metric='alivenodes').set(get_numAliveNodes(url))
    e.state('stopped')
