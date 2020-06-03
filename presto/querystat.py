# -*- coding:utf-8 -*-

import requests
import time
import json

print(time.strftime("%Y-%m-%d %H:%M:%S"))


def getQueryList(url):
    request = requests.get(url)
    data = request.json()
    return data


def getRunningQueryId(data):
    idList = []
    for query in data:
        state = query['state']
        currtime = int(time.time() * 1000)
        startime = query['session']['startTime']
        timevalue = currtime - startime
        if state == 'RUNNING' and timevalue > 600000:
            querystatement = query['query']
            queryid = (query['queryId'])
            print(sendtodd(timevalue, currtime, queryid,querystatement))
            idList.append(queryid)
    return idList


def killQuery(queryid):
    url = 'http://10.89.90.212:8285/v1/query/%s/killed' % (queryid)
    request = requests.put(url)
    code = request.status_code
    return code


def sendtodd(timevalue, currtime, id,query):
    url = 'https://oapi.dingtalk.com/robot/send?access_token=866fae431fee6ac9c5cd94a47cbc90d28df86de0b07cc3686667e8416fc08495'
    data={'msgtype': 'text',
     'text': {
         'content':'触发报警：问题sql \n \n状态：Killed \n \n执行时长：%s ms\n \n发生时间：%s \n \nQueryId: %s \n \n相关SQL：%s' % (timevalue, currtime, id,query)
     }
     }
    print(data)
    request = requests.post(url, headers={'Content-Type':'application/json;charset=utf-8'}, data=json.dumps(data))
    return request.status_code


if __name__ == '__main__':

    url = 'http://10.89.90.212:8285/v1/query'
    querylist = getQueryList(url)
    print(querylist)
    #idlist = getRunningQueryId(querylist)
    #for queryid in idlist:
    #    killQuery(queryid)


"""
for query in data:
    # print(query['state'])
    state = query['state']
    currtime = int(time.time() * 1000)
    startime = query['session']['startTime']
    timevalue = currtime - startime
    # (timevalue)
    if state == 'RUNNING' and timevalue >= 600:
        print(timevalue)
        # if query['queryStats']['executionTime']
        # print("Runing sql")
        print (query)
        print(query['queryId'])
        #queryid = query['queryId']
        #idList.append(queryid)
"""
