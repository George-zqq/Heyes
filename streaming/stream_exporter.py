# -*- utf-8 -*-
import json
import requests
from flask import Flask,Response
from prometheus_client import Gauge,CollectorRegistry,generate_latest
from configparser import ConfigParser
config = ConfigParser()
config.readfp(open('./config.ini'))
url = config.get('yarn_api_master','url')

app = Flask(__name__)

appslist = ['ClassroomMonitor_real',
        'DeviceException_real',
        'htp_real',
        'smalltopics_real',
        'logandtracker_real',
        'gameserver_real',
        'mq2hive_real',
        'lesson_pre_real',
        'lesson_mid_real',
        'lesson_midq_real',
        'lesson_version_real',
        'scouta_uv_real',
        'break_point_real',
        'htp_deviceInfo_real',
        'share_monitor_real',
        'audition_midq_real',
        'audition_mid_real',
        'htp_gsjoinleave_real',
        'htp_ai_tracker_real',
        'htp_ai_crexcept_real',
        'htp_ai_performce_real',
        'techlog_real',
        'timeline_real',
        'classroom_user_monitor',
        'classroom_net_monitor',
        'classroom_join_monitor',
        'htp_ai_crexcept_real',
        'htp_ai_cliexcept_real',
        'notice_real',
        'oper-firstscreen-real',
        'oper-netrequest-real',
        'oper-soundnetwork-real',
        'oper-faulttrace-real']

Registry = CollectorRegistry()

appsState = Gauge('app_streaming_state', 'Descriptionofgauge', ['name'], registry=Registry)
appsDelay = Gauge('app_streaming_delay','Descriptionofgauge', ['name'], registry=Registry)
appsBatch = Gauge('app_streaming_batches','Descriptionofgauge',['name'],registry=Registry)
appsTime = Gauge('app_streaming_starttime','Descriptionofgauge',['name'],registry=Registry)
appsReceived = Gauge('app_streaming_Received','Descriptionofgauge',['name'],registry=Registry)

@app.route('/metrics/stream')
def get_appstate():
    downapplist,appdata = get_applist()

    for appname in appslist:
        if appname in downapplist:
            for data in appdata:
                if data['name'] == appname and data['state']=='RUNNING':
                    appsState.labels(name=appname).set('1')
                    appid = data['id']
                    numTotalCompletedBatches, startTime, avgTotalDelay, numReceivedRecords = get_appdelay(appid)
                    appsDelay.labels(name=appname).set(avgTotalDelay)
                    appsBatch.labels(name=appname).set(numTotalCompletedBatches)
                    #appsTime.labels(name=appname).set(startTime)
                    appsReceived.labels(name=appname).set(numReceivedRecords)
                else:
                    continue
        else:
            appsState.labels(name=appname).set('0')
    return Response(generate_latest(Registry), mimetype='text/plain')


def get_applist():
    downloadlist = []
    Url = '%s/ws/v1/cluster/apps?states=running&applicationTypes=SPARK' % (url)
    request = requests.get(Url)
    appdata = request.json()['apps']['app']
    for appinfo in appdata:
        downloadlist.append(appinfo['name'])
    return downloadlist,appdata


def get_appdelay(appid):
    delayUrl = '%s/proxy/%s/api/v1/applications/%s/streaming/statistics' % (url,appid,appid)
    print(delayUrl)
    request = requests.get(delayUrl)
    numTotalCompletedBatches = request.json()['numTotalCompletedBatches']
    startTime = request.json()['startTime']
    avgTotalDelay = request.json()['avgTotalDelay']
    numReceivedRecords = request.json()['numReceivedRecords']
    return numTotalCompletedBatches,startTime,avgTotalDelay,numReceivedRecords


if __name__=="__main__":

    app.run(host='0.0.0.0',port=8005)



