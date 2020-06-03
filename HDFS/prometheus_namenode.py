#!-*- coding:utf-8 -*-

from prometheus_client import Gauge, Counter, Enum, CollectorRegistry
import requests
import subprocess
import time


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
        data = self.session.json()['beans'][7]
        capacityUsedGB = data['CapacityUsedGB']
        capacityTotalGB = data['CapacityTotalGB']
        utilization = capacityUsedGB / capacityTotalGB
        return '%.4f' % utilization

    def get_dfs_corruptedBlocks(self):
        data = self.session.json()['beans'][7]
        corrBlock = data['CorruptBlocks']
        return corrBlock

    def get_nn_rpcConn(self):
        data = self.session.json()['beans'][37]
        rpcConnNum = data['NumOpenConnections']
        return rpcConnNum

    def get_dfs_totalFiles(self):
        data = self.session.json()['beans'][7]
        totalFiles = data['TotalFiles']
        return totalFiles

    def get_dfs_totalBlocks(self):
        data = self.session.json()['beans'][7]
        totalBlocks = data['BlocksTotal']
        return totalBlocks

    def get_dfs_UnderReplicatedBlocks(self):
        data = self.session.json()['beans'][7]
        urBlocks = data['UnderReplicatedBlocks']
        return urBlocks

    def get_dfs_missBlocks(self):
        data = self.session.json()['beans'][7]
        missBlocks = data['MissingBlocks']
        return missBlocks

    def get_dfs_excessBlocks(self):
        data = self.session.json()['beans'][7]
        exBlocks = data['ExcessBlocks']
        return exBlocks

    def get_dfs_LastCheckpointTime(self):
        data = self.session.json()['beans'][7]
        lcpTime = data['LastCheckpointTime']/1000
        #lcptime = time.localtime(lcpTime)
        #lcptime = str(time.strftime("%Y-%m-%d %H:%M:%S", lcptime))
        return lcpTime

    def get_numAliveNodes(self):
        data = self.session.json()['beans'][32]
        numNodes = data['NumLiveDataNodes']
        return numNodes

    def get_numDeadNodes(self):
        data = self.session.json()['beans'][32]
        numdead = data['NumDeadDataNodes']
        return numdead

    def get_staleNodes(self):
        data = self.session.json()['beans'][32]
        stale = data['NumStaleDataNodes']
        return stale

    def get_lastHaTrans(self):
        data = self.session.json()['beans'][25]
        lastTrans = data['LastHATransitionTime']
        return lastTrans

    # number of xceiver
    def get_TotalLoad(self):
        data = self.session.json()['beans'][7]
        totaload = data['TotalLoad']
        return totaload

    def get_receivedBytes(self):
        data = self.session.json()['beans'][37]
        receivedBytes = data['ReceivedBytes']
        return receivedBytes

    def get_sentdBytes(self):
        data = self.session.json()['beans'][37]
        sentdBytes = data['SentBytes']
        return sentdBytes

    def get_capacityRemainingGB(self):
        data = self.session.json()['beans'][7]
        capacityRemainGB = data['CapacityRemainingGB']

        return capacityRemainGB

    def get_capacityUsedGB(self):
        data = self.session.json()['beans'][7]
        capacityUsedGB = data['CapacityUsedGB']
        return capacityUsedGB

    def get_capacityTotalGB(self):
        data = self.session.json()['beans'][7]
        capacityTotalGB = data['CapacityTotalGB']
        return capacityTotalGB

    def get_blockCapacity(self):
        data = self.session.json()['beans'][7]
        blockCapacity = data['BlockCapacity']
        return blockCapacity

    def get_PendingDeletionBlocks(self):
        data = self.session.json()['beans'][7]
        num = data['PendingDeletionBlocks']
        return num

    def get_numTimedOutPendingReplications(self):
        data = self.session.json()['beans'][7]
        num = data['NumTimedOutPendingReplications']
        return num

    def get_numActiveClients(self):
        data = self.session.json()['beans'][7]
        num = data['NumActiveClients']
        return num

    def get_MissingReplOneBlocks(self):
        data = self.session.json()['beans'][7]
        num = data['MissingReplOneBlocks']
        return num

    def get_jvm_ThreadsNew(self):
        data = self.session.json()['beans'][0]
        num = data['ThreadsNew']
        return num

    def get_jvm_ThreadsRunnable(self):
        data = self.session.json()['beans'][0]
        num = data['ThreadsRunnable']
        return num

    def get_jvm_ThreadsBlocked(self):
        data = self.session.json()['beans'][0]
        num = data['ThreadsBlocked']
        return num

    def get_jvm_ThreadsWaiting(self):
        data = self.session.json()['beans'][0]
        num = data['ThreadsWaiting']
        return num

    def get_jvm_ThreadsTimedWaiting(self):
        data = self.session.json()['beans'][0]
        num = data['ThreadsTimedWaiting']
        return num

    def get_jvm_ThreadsTerminated(self):
        data = self.session.json()['beans'][0]
        num = data['ThreadsTerminated']
        return num




    @property
    def get_zfkcStatus(self):
        pidpipe = subprocess.Popen("jps | grep DFSZKFailoverController", stdout=subprocess.PIPE)
        pid = pidpipe.communicate(pidpipe.stdout)
        if pid:
            status = 'running'
        else:
            status = 'stopped'
        return status


exporter = hdfsExporter(url='http://bdp02.sa.cn:50070/jmx')
print(exporter.get_numTimedOutPendingReplications())
# a = Gauge('namenode', 'Descriptionofgauge', ['cluster', 'service', 'metric'], registry=Registry)
# b = Gauge('dfsblockscorrupt', 'Corrupted Block Number', ['cluster', 'service', 'metric'], registry=Registry)
# c = Gauge('dfsNumNodes', 'Alive Nodes', ['cluster', 'service', 'metric'], registry=Registry)
# e = Enum('my_task_state', 'Description of enum',states=['starting', 'running', 'stopped'])

# a.labels(cluster='bdp', service='bdp102', metric='heapuse').set(exporter.get_nnHeap_utilization())
# b.labels(cluster='bdp', service='hdfs', metric='repblock').set(exporter.get_dfs_corruptedRep())
# c.labels(cluster='bdp', service='hdfs', metric='alivenodes').set(exporter.get_numAliveNodes())
# e.state('stopped')
