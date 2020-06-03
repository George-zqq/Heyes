# -*- coding -*-

#from YARN import qry
import requests
import json


class yarnexporter(object):
    def __init__(self, url):
        self.url = url
        self.session = requests.session()
        # self.qry = qry.yarnjmx

    def get_valueRpcActivityForPort(self):
        query = 'Hadoop:service=ResourceManager,name=RpcActivityForPort8031'
        url = "%s?qry=%s" % (self.url, query)
        data = self.session.get(url).json()['beans'][0]
        ReceivedBytes = data['ReceivedBytes']
        SentBytes = data['SentBytes']
        NumOpenConnections = data['NumOpenConnections']
        return ReceivedBytes, SentBytes, NumOpenConnections

    def get_rmJvmMetric(self):
        query = "Hadoop:service=ResourceManager,name=JvmMetrics"
        url = "%s?qry=%s" % (self.url, query)
        print(str(url))
        data = self.session.get(url).json()['beans'][0]
        """
        MemNonHeapUsedM = data['MemNonHeapUsedM']
        MemHeapUsedM = data ['MemHeapUsedM']
        GcCount = data['GcCount']
        ThreadsNew = data['ThreadsNew']
        ThreadsRunnable = data['ThreadsRunnable']
        ThreadsBlocked = data['ThreadsBlocked']
        ThreadsWaiting = data['ThreadsWaiting']
        ThreadsTimedWaiting = data['ThreadsTimedWaiting']
        ThreadsTerminated = data['ThreadsTerminated']
        """
        return data

    def get_queueMetric(self):
        query = 'Hadoop:service=ResourceManager,name=QueueMetrics,q0=root'
        url = '%s?qry=%s' % (self.url, query)
        data = self.session.get(url).json()['beans'][0]
        """
        appRunning = data['AppsRunning']
        appPending = data['AppsPending']
        appsSubmitted = data['AppsSubmitted']
        appsCompleted = data['AppsCompleted']
        appsKilled = data['AppsKilled']
        appsFailed = data['AppsFailed']
        allocatedMB = data['AllocatedMB']
        allocatedVCores = data['AllocatedVCores']
        allocatedContainers = data['AllocatedContainers']
        availableMB = data['AvailableMB']
        availableVCores = data['AvailableVCores']
        pendingMB = data['PendingMB']
        pendingVCores = data['PendingVCores']
        pendingContainers = data['PendingContainers']
        reservedMB = data['ReservedMB']
        reservedVCores = data['ReservedVCores']
        reservedContainers = data['ReservedContainers']
        """
        return data

    def get_rnnminfo(self):
        query = 'Hadoop:service=ResourceManager,name=RMNMInfo'
        url = "%s?qry=%s" % (self.url, query)
        data = self.session.get(url).json()['beans'][0]
        data = data['LiveNodeManagers']
        return json.loads(data)



'''
yarnexporter = yarnexporter('http://bdp02.sa.cn:8088/jmx')
print(yarnexporter.get_rnnminfo())

metricdata = (yarnexporter.get_rnnminfo())


for metric in metricdata:
    host = metric['HostName']
    lasthealth = metric['LastHealthUpdate']
    numcontainer = metric['NumContainers']
    useMemMB = metric['UsedMemoryMB']
    avaiMemMB = metric['AvailableMemoryMB']
    print(host,lasthealth,numcontainer,useMemMB,avaiMemMB)
'''