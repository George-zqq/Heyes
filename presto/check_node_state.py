# -*- coding : utf-8 -*-
# /usr/bin/env python


import requests
from prometheus_client import CollectorRegistry, generate_latest, Enum,Gauge
from flask import Flask, Response

app = Flask(__name__)

REGISTRY = CollectorRegistry(auto_describe=False)

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
    "bdp-presto11": "10.89.89.192",
    "bdp-presto12": "10.89.93.95",
    "bdp-presto13": "10.89.93.53",
    "bdp-presto14": "10.89.93.84",
    "bdp-presto15": "10.89.93.122",
    "bdp-presto16": "10.89.93.143"
}

@app.route('/metrics/presto_state')
def getnodeState():
    REGISTRY = CollectorRegistry()
    g = Gauge('presto_state', 'worker state', ['host'], registry=REGISTRY)
    for host in ipdict.keys():

        ip = ipdict.get(host)
        url = "http://%s:8285/v1/info/state" % (ip)
        print(url)
        print(host)
        try:
            state = requests.get(url, timeout=5)
            print(state.status_code)

        except Exception:

            g.labels(host=host).set("0")

            continue

        if state.status_code == 200 and state.json() == 'v':

            g.labels(host=host).set("1")

        else:
            g.labels(host=host).set("0")

    return Response(generate_latest(REGISTRY), mimetype='text/plain')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8002)
