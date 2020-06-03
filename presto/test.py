import requests
import json
url = 'https://oapi.dingtalk.com/robot/send?access_token=866fae431fee6ac9c5cd94a47cbc90d28df86de0b07cc3686667e8416fc08495'
data={'msgtype': 'text',
     'text': {
         'content':{'触发报警：问题sql \n \n状态：Killed \n \n执行时长：%s ms\n \n发生时间：%s \n \nQueryId: %s \n \nSql信息：null'}
     }
     }
print(data)
request = requests.post(url, headers={'Content-Type':'application/json;charset=utf-8'}, data=json.loads(data))