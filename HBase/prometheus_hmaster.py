# -*- coding : utf-8

import requests
from flask import Response, Flask
from prometheus_client import Enum, CollectorRegistry, generate_latest

app = Flask(__name__)

REGISTRY = CollectorRegistry(auto_describe=False)

e = Enum('namenode_state', 'namenode status', states=['running', 'stopped'])
e.state('running')




class hbase_exporter(object):
    def __init__(self, url):
        self.url = url
        self.session = requests.session().get(self.url)

    def get_averageLoad(self):
        request = self.session.json()
        load = request['beans']
        return load

    def get_RitCount(self):
        request = self.session.json()
        return request

    def getHeapUtilization(self):
        return

    def getReceiveBytes(self):
        return

    def getSentByte(self):
        return

    def getOpenFileCount(self):
        return

    def getProcessLoad(self):
        return

    def getAvalableProcessor(self):
        return

    def getHMsystemLoadAverage(self):
        return

    def getFreeMemory(self):
        return

    def getClusterRequests(self):
        return

    def getMemStoreHitCount(self):
        return

    def memStoreSizeMB(self):
        return

    def getStores(self):
        return

    def storeFileSizeMB(self):
        return

    def getStoreFiles(self):
        return


url = 'http://bdp103.qa.sa.cn:16010/jmx'
ex = hbase_exporter(url)

data = ex.get_averageLoad()

print(data)
