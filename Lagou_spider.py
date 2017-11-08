import requests
import json
from bs4 import BeautifulSoup as bs
import time
headers = {
    'Host': 'www.lagou.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
    'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
    'Connection': 'keep-alive',
    'Cache-Control': 'no-cache',
    'X-Anit-Forge-Code':'0',
    'X-Anit-Forge-Token':None,
    'X-Requested-With':'XMLHttpRequest'
}
url1 = "https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false&isSchoolJob=0"
positions = []
for x in range(1,5):
    form_data = {
        'first': 'true',
        'pn': x,
        'kd': 'python'
    }
    res = requests.post(url1,headers=headers,data=form_data)
    soup = bs(res.text,'html.parser')
    jd = json.loads(res.text)
    infos = jd['content']['positionResult']['result']
    positions.extend(infos)
    time.sleep(5)
    print('----'*40)
    print("当前爬取到的是第 %s 页的信息" % x)
    print(infos)
    print('----'*40)

