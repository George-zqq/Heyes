# -*- coding:utf-8 -*-

from flask import Response, Flask
import requests
from prometheus_client import Gauge, CollectorRegistry, generate_latest

app = Flask(__name__)

REGISTRY = CollectorRegistry(auto_describe=False)

a = Gauge('PrestoRunningQueries', 'num 0f running Queries', ['cluster', 'host'], registry=REGISTRY)
b = Gauge('PrestoBlockedQueries', 'num 0f block Queries', ['cluster', 'host'], registry=REGISTRY)
c = Gauge('PrestoQueuedQueries', 'num 0f queue Queries', ['cluster', 'host'], registry=REGISTRY)
d = Gauge('PrestoActiveWorkers', 'num 0f Active workers', ['cluster', 'host'], registry=REGISTRY)
e = Gauge('PrestoRunningDrivers', 'num 0f running drivers', ['cluster', 'host'], registry=REGISTRY)
g = Gauge('PrestoReservedMemory', 'sum 0f Mem', ['cluster', 'host'], registry=REGISTRY)


@app.route('/metric/presto')
def getprestoInfo():
    url = 'http://10.89.90.212:8285/v1/cluster'
    request = requests.get(url)
    data = request.json()
    runningQueries = data['runningQueries']
    blockedQueries = data['blockedQueries']
    queuedQueries = data['queuedQueries']
    activeWorkers = data['activeWorkers']
    runningDrivers = data['runningDrivers']
    reservedMemory = data['reservedMemory'] / 1024 / 1024
    # totalInputRows = data['totalInputRows']
    # totalInputBytes = data['totalInputBytes']
    a.labels(cluster='online', host='bdp-presto01').set(runningQueries)
    b.labels(cluster='online', host='bdp-presto01').set(blockedQueries)
    c.labels(cluster='online', host='bdp-presto01').set(queuedQueries)
    d.labels(cluster='online', host='bdp-presto01').set(activeWorkers)
    e.labels(cluster='online', host='bdp-presto01').set(runningDrivers)
    g.labels(cluster='online', host='bdp-presto01').set(reservedMemory)
    return Response(generate_latest(REGISTRY), mimetype='text/plain')


def getnodeInfo():
    url = 'http://10.89.90.212:8285/v1/query-execution'
    request = requests.get(url)
    data = request.json()
    print(data)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000)
    #getnodeInfo()
