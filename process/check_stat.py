#!/bin/python
from flask import Response, Flask
import subprocess
import socket
from process.config import hadoop
from prometheus_client import CollectorRegistry, generate_latest, Enum

app = Flask(__name__)


@app.route('/metric/hadoop_service_state')
def process_exporter():
    from process.config import hadoop
    host = socket.gethostname()
    REGISTRY = CollectorRegistry(auto_describe=True)
    servicelist = hadoop.get(host)
    for service in servicelist:
        metricname = 'process_' + service + '_state'
        state = int(service_state(service).strip())
        print(state)
        print(type(state))

        if state >= 1:
            e = Enum(metricname, 'process status', states=['running'], registry=REGISTRY)
            e.state('running')
        elif state == 0:
            e = Enum(metricname, 'process status', states=['stopped'], registry=REGISTRY)
            e.state('stopped')
        else:
            e = Enum(metricname, 'process status', states=['Nostate'], registry=REGISTRY)
            e.state("Nostate")
    return Response(generate_latest(REGISTRY), mimetype='text/plain')


def get_serviceList():
    host = socket.gethostname()
    servicelist = hadoop.get(host)
    return servicelist


def service_state(service):
    cmd = "ps -ef | grep %s |grep -v grep |  wc -l" % (service)
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    code, err = process.communicate()
    return code


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8010)
