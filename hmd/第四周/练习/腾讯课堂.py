# -*- coding：utf-8 -*-
"""
%Author     :hmd
%FileName   :腾讯课堂.py
%Time       :2022/10/25 8:45
"""
"""
练习目的：
tengxun.  使用requests库或者selenium库请求网页信息
2.  跟据返回内容选择恰当的数据解析方法解析数据
3.  将数据存储到csv文件中
4.  注意翻页
"""
# 导包
import requests
import csv
from lxml import html

# 链接
url = "https://ke.qq.com/"
# 请求头信息
header = {
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
}
# 请求网页
response = requests.get(url,headers=header)
# 指定编码格式
response.encoding = "utf-8"
# 转化文档数对象
page1 = html.etree.HTML(response.text)
# 得到最后一页的的页数  ----34
page_li = page1.xpath('//ul[@unselectable="unselectable"]//a[@rel="nofollow"]/text()')
page_num = int(page_li[-1])
print(page_num)










