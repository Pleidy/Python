
import requests
import urllib, httplib2
import urllib.parse
import json
#青云客智能聊天机器人
def qyk():
    content = {'key': 'free', 'appid': 0, 'msg': '你好'}
    r = requests.get(url='http://api.qingyunke.com/api.php', params=content)
    a = json.loads(r.text).get('content')
    print(a)

qyk()

