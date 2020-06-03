# -*- utf-8 -*-
import json
import requests
from flask import Flask
from prometheus_client import Gauge,CollectorRegistry
from configparser import ConfigParser
config = ConfigParser()
config.readfp(open('./config.ini'))
url = config.get('yarn_api_master','url')

applist = ['ClassroomMonitor_real',
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


url = 'http://bdp01.sa.cn:8088/ws/v1/cluster/apps?states=running&applicationTypes=SPARK'
#url = 'http://bdp01.qa.sa.cn:8088/proxy/application_1588161284167_297710/api/v1/applications/application_1588161284167_297710/streaming/statistics'
request = requests.get(url)
appdata = request.json()['apps']['app']

for app in appdata:
    print(type(app))
    for key in app.iterkeys():
        print(key)
0


