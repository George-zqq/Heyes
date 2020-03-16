# -*- coding:utf-8 -*-

from flask import Response, Flask
import requests
from prometheus_client import Gauge, CollectorRegistry, generate_latest, Enum

app = Flask(__name__)


@app.route('/metric/presto')
def getprestoInfo():
    REGISTRY = CollectorRegistry(auto_describe=False)

    a = Gauge('PrestoRunningQueries', 'num 0f running Queries', ['cluster', 'host'], registry=REGISTRY)
    b = Gauge('PrestoBlockedQueries', 'num 0f block Queries', ['cluster', 'host'], registry=REGISTRY)
    c = Gauge('PrestoQueuedQueries', 'num 0f queue Queries', ['cluster', 'host'], registry=REGISTRY)
    d = Gauge('PrestoActiveWorkers', 'num 0f Active workers', ['cluster', 'host'], registry=REGISTRY)
    e = Gauge('PrestoRunningDrivers', 'num 0f running drivers', ['cluster', 'host'], registry=REGISTRY)
    g = Gauge('PrestoReservedMemory', 'sum 0f Mem', ['cluster', 'host'], registry=REGISTRY)
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


ipdict = {
    "bdp-presto01": "10.89.90.212",
    "bdp-presto02": "10.89.90.226",
    "bdp-presto03": "10.89.90.218",
    "bdp-presto04": "10.89.90.198",
    "bdp-presto05": "10.89.90.224",
    "bdp-presto06": "10.89.90.207",
    "bdp-presto07": "10.89.90.183",
    "bdp-presto08": "10.89.90.187",
    "bdp-presto09": "10.89.90.235",
    "bdp-presto10": "10.89.89.210",
    "bdp-presto11": "10.89.89.192"
}


@app.route('/metric/presto_worker_state')
def getnodeState():
    REGISTRY = CollectorRegistry(auto_describe=True)
    for host in ipdict.keys():
        ip = ipdict.get(host)
        metricname = host[4:]
        url = "http://%s:8285/v1/info/state" % (ip)
        print(url)
        print(host)
        try:
            state = requests.get(url, timeout=5)

            if state.json() == 'ACTIVE':
                e = Enum(metricname, 'presto worker state', states=['Active'], registry=REGISTRY)
                e.state("Active")

            else:
                e = Enum(metricname, 'presto worker state', states=['Dead'], registry=REGISTRY)
                e.state('Dead')
        except Exception:
            e = Enum(metricname, 'presto worker state', states=['Dead'], registry=REGISTRY)
            e.state('Dead')
    return Response(generate_latest(REGISTRY), mimetype='text/plain')


def getnodeInfo():
    url = 'http://10.89.90.212:8285/v1/query-execution'
    request = requests.get(url)
    data = request.json()
    print(data)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000)
    # getnodeInfo()
