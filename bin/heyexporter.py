# -*- coding:utf-8 -*-
import sys
from HDFS.prometheus_namenode import hdfsExporter
from flask import Response, Flask
from prometheus_client import Gauge, Counter, Enum, CollectorRegistry, generate_latest
from configparser import ConfigParser

app = Flask(__name__)

config = ConfigParser()
config.readfp(open('../conf/config.ini'))
url = config.get('dfs_jmx_url', 'url')


@app.route('/metric/dfs')
def dfsmetric():
    Registry = CollectorRegistry()
    dfsurl = config.get('dfs_jmx_url', 'url')
    exporter = hdfsExporter(dfsurl)

    a = Gauge('namenode', 'Descriptionofgauge', ['cluster', 'service', 'metric'], registry=Registry)
    b = Gauge('dfsblockscorrupt', 'Corrupted Block Number', ['cluster', 'service', 'metric'], registry=Registry)
    c = Gauge('dfsNumNodes', 'Alive Nodes', ['cluster', 'service', 'metric'], registry=Registry)

    a.labels(cluster='bdp', service='bdp102', metric='heapuse').set(exporter.get_nnHeap_utilization())
    b.labels(cluster='bdp', service='hdfs', metric='repblock').set(exporter.get_dfs_corruptedRep())
    c.labels(cluster='bdp', service='hdfs', metric='alivenodes').set(exporter.get_numAliveNodes())

    return Response(generate_latest(Registry), mimetype='text/plain')


#@app.route('/metric/yarn')
#def yarnmetric():
    #return Response(generate_latest(Registry), mimetype='text/plain')


#@app.route('/metric/hive')
#def hivemetric():
   # return Response(generate_latest(Registry), mimetype='text/plain')


#@app.route('/metric/hbase')
#def hbasemetric():
  #  return Response(generate_latest(Registry), mimetype='text/plain')


#@app.route('/metric/zk')
#def zkmetric():
 #   return Response(generate_latest(Registry), mimetype='text/plain')


#@app.route('/metric/presto')
#def prestometric():
#    return Response(generate_latest(Registry), mimetype='text/plain')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8765)

