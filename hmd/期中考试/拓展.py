# -*- coding��utf-8 -*-
"""
%Author     :hmd
%FileName   :��չ.py
%Time       :2022/11/23 15:51
"""
import requests
import  csv
import json
url = "https://so.csdn.net/api/v3/search?q=python&t=all&p=1&s=0&tm=0&lv=-1&ft=0&l=&u=&ct=-1&pnt=-1&ry=-1&ss=-1&dct=-1&vco=-1&cc=-1&sc=-1&akt=-1&art=-1&ca=-1&prs=&pre=&ecc=-1&ebc=-1&ia=1&dId=&cl=-1&scl=-1&tcl=-1&platform=pc"
header = {
'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.3'
}
resp = requests.get(url=url,headers=header)
a = resp.text
info = json.loads(a)
# print(info,type(info))
info1 = info["result_vos"]
with open('csdn.csv',"w+",newline='') as f:
    infomation = csv.writer(f)
    one = ['����','����']
    infomation.writerow(one)

    for item in info1:
        title = item["title"]
        new_title = title.replace('<em>','').replace('</em>','')
        link = item["url"]
       # �ҵ�90��
        for j in range(1,91):
            last_rank = f'heeps://edu.csdn.net'
        infomation.writerow(two)
        print(new_title,link)
