# -*- coding:utf-8 -*-
import sys
from HDFS.prometheus_namenode import hdfsExporter
from flask import Response, Flask
from prometheus_client import Gauge, Counter, Enum, CollectorRegistry,generate_latest
from configparser import ConfigParser



app = Flask(__name__)
Registry = CollectorRegistry()


@app.route('/metric/dfs')
def dfsmetric(registry):
    return Response(generate_latest(registry), mimetype='text/plain')
