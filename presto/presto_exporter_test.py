# -*- coding : utf-8

import requests
from prometheus_client import start_http_server, Gauge, Counter, Enum, CollectorRegistry
import time
from prometheus_client.core import CollectorRegistry
from flask import Response, Flask


# url = 'http://10.89.90.207:8285/v1/cluster'

def getprestoInfo(url):
    request = requests.get(url)
    data = request.json()
    return data


# print(runningDrivers,runningQueries,blockedQueries,queuedQueries,activeWorkers,activeWorkers,reservedMemory,totalInputRows,totalInputBytes)
# inputrow = Counter()


if __name__ == '__main__':

    url = 'http://10.89.90.212:8285/v1/cluster'

    a = Gauge('PrestoRunningQueries', 'num 0f running Queries', ['cluster', 'host'])
    b = Gauge('PrestoBlockedQueries', 'num 0f block Queries', ['cluster', 'host'])
    c = Gauge('PrestoQueuedQueries', 'num 0f queue Queries', ['cluster', 'host'])
    d = Gauge('PrestoActiveWorkers', 'num 0f Active workers', ['cluster', 'host'])
    e = Gauge('PrestoRunningDrivers', 'num 0f running drivers', ['cluster', 'host'])
    g = Gauge('PrestoReservedMemory', 'sum 0f Mem', ['cluster', 'host'])
    start_http_server(8001)

    while True:
        data = getprestoInfo(url)
        runningQueries = data['runningQueries']
        blockedQueries = data['blockedQueries']
        queuedQueries = data['queuedQueries']
        activeWorkers = data['activeWorkers']
        runningDrivers = data['runningDrivers']
        reservedMemory = data['reservedMemory']
        totalInputRows = data['totalInputRows']
        totalInputBytes = data['totalInputBytes']
        a.labels(cluster='online', host='bdp-presto01').set(runningQueries)
        b.labels(cluster='online', host='bdp-presto01').set(blockedQueries)
        c.labels(cluster='online', host='bdp-presto01').set(queuedQueries)
        d.labels(cluster='online', host='bdp-presto01').set(activeWorkers)
        e.labels(cluster='online', host='bdp-presto01').set(runningDrivers)
        g.labels(cluster='online', host='bdp-presto01').set(reservedMemory)
        time.sleep(0.5)
