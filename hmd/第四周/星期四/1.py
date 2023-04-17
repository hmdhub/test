# -*- coding：utf-8 -*-
"""
%Author     :hmd
%FileName   :tengxun.py
%Time       :2022/10/20 10:49
"""
import requests
from lxml import html
import json
import csv

url = "https://www.douyin.com/aweme/v1/web/page/data/?device_platform=webapp&aid=6383&channel=channel_pc_web&module_count=2&spider=0&pc_client_type=tengxun&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1280&screen_height=720&browser_language=zh-CN&browser_platform=Win32&browser_name=Chrome&browser_version=105.0.0.0&browser_online=true&engine_name=Blink&engine_version=105.0.0.0&os_name=Windows&os_version=10&cpu_core_num=8&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=50&webid=7156415344294561320&msToken=eZoxGSe6gpkoYaNYNhJr99p-97b7j9gTiUv3BL4nK781nYZWH2WbrTDG8JXgdil23suUpLbZyq_4tTZ7Vs2GzsOFT_kT2jJhgZC9IKtcMzHTlJHaboDgaAA=&X-Bogus=DFSzswVOJczANH89S/vr5F9WX7jn"
header = {
'user-agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
}
resp = requests.get(url,headers=header)
# 获取网页源码
page = resp.text
# print(page)   # 字符串
# 使用json模块
info = json.loads(page)
# print(info)   # 字典类型
# print(type(page),type(info))

# 字典取值
module_list = info['data']['module_list']

for item in module_list:
    module = item['word']
    print(module)









