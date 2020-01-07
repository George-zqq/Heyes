import requests

ROOT_URL = 'https://www.instagram.com/ponysmakeup'
PROXY = {'http':'george:zqq7990@http://144.34.211.5.16.9887','https':'george:zqq7990@https://144.34.211.5.16.9887'}

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36',
    'Cookie': 'csrftoken=CJFcAbgR8qC0IGukQRh2rUtkwgimlH4m'
}
USERNAME = 'ponysmakeup'

re = requests.get(ROOT_URL,proxies=PROXY,headers=HEADERS)
re.encoding = 'utf-8'
print(re.text)

