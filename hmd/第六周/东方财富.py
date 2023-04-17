# -*- coding：utf-8 -*-
"""
%Author     :hmd
%FileName   :东方财富 基金网.py
%Time       :2022/11/4 11:31
"""
import requests
import json
url = "http://fund.eastmoney.com/data/rankhandler.aspx?op=dy&dt=kf&ft=all&rs=&gs=0&sc=qjzf&st=desc&sd=2021-11-04&ed=2022-11-04&es=0&qdii=&pi=1&pn=50&dx=0&v=0.033354615825327505"
header = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
}
res = requests.get(url,headers = header)
res.encoding = 'utf-8'

