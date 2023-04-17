# -*- coding：utf-8 -*-
"""
%Author     :hmd
%FileName   :初级实现.py
%Time       :2022/11/23 14:06
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
    one = ['标题','链接']
    infomation.writerow(one)

    for item in info1:
        title = item["title"]
        new_title = title.replace('<em>','').replace('</em>','')
        link = item["url"]

        if title:
            new_title=new_title
        else:
            new_title=''
        if link:
            link=link
        else:
            link=''
        two =[new_title,link]
        infomation.writerow(two)
        print(new_title,link)



