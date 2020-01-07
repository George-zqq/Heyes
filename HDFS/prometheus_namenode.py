#!-*- coding:utf-8 -*-

from prometheus_client import Gauge, Counter, Enum, CollectorRegistry
import requests
import subprocess


# url = 'http://bdp102.qa.sa.cn:50070/jmx'


class hdfsExporter(object):
    def __init__(self, url):
        self.url = url
        self.session = requests.session().get(self.url)

    def get_nnHeap_utilization(self):
        data = self.session.json()['beans'][0]
        memmax = data['MemHeapMaxM']
        memused = data['MemHeapUsedM']
        utilization = memused / memmax
        return '%.2f' % utilization

    def get_dfs_utilization(self):
        data = self.session.json()['beans'][8]
        capacityUsedGB = data['CapacityUsedGB']
        capacityTotalGB = data['CapacityTotalGB']
        utilization = capacityUsedGB / capacityTotalGB
        return '%.4f' % utilization

    def get_dfs_corruptedRep(self):
        data = self.session.json()['beans'][8]
        corrBlock = data['CorruptBlocks']
        return corrBlock

    def get_nn_rpcConn(self):
        data = self.session.json()['beans'][37]
        rpcConnNum = data['NumOpenConnections']
        return rpcConnNum

    def get_dfs_totalFiles(self):
        data = self.session.json()['beans'][8]
        totalFiles = data['TotalFiles']
        return totalFiles

    def get_dfs_totalBlocks(self):
        data = self.session.json()['beans'][8]
        totalBlocks = data['BlocksTotal']
        return totalBlocks

    def get_numAliveNodes(self):
        data = self.session.json()['beans'][32]
        numNodes = data['NumLiveDataNodes']
        return numNodes

    def get_zfkcStatus(self):
        pidpipe = subprocess.Popen("jps | grep DFSZKFailoverController",stdout=subprocess.PIPE)
        pid = pidpipe.communicate(pidpipe.stdout)
        if pid:
            status = 'running'
        else:
            status = 'stopped'
        return status

# exporter = hdfsExporter(url='http://bdp102.qa.sa.cn:50070/jmx')
# a = Gauge('namenode', 'Descriptionofgauge', ['cluster', 'service', 'metric'], registry=Registry)
# b = Gauge('dfsblockscorrupt', 'Corrupted Block Number', ['cluster', 'service', 'metric'], registry=Registry)
# c = Gauge('dfsNumNodes', 'Alive Nodes', ['cluster', 'service', 'metric'], registry=Registry)
# e = Enum('my_task_state', 'Description of enum',states=['starting', 'running', 'stopped'])

# a.labels(cluster='bdp', service='bdp102', metric='heapuse').set(exporter.get_nnHeap_utilization())
# b.labels(cluster='bdp', service='hdfs', metric='repblock').set(exporter.get_dfs_corruptedRep())
# c.labels(cluster='bdp', service='hdfs', metric='alivenodes').set(exporter.get_numAliveNodes())
# e.state('stopped')
