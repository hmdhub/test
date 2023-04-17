# -*- coding：utf-8 -*-
"""
%Author     :hmd
%FileName   :上午上课笔记.py
%Time       :2022/9/30 10:08
"""
# 步骤
# tengxun.导包
# 2.抓包
# 3.使用requests进行请求
# 4.获取响应文本信息
# 5.转换文档树类型
# 6.使用xpath匹配所需信息
import requests
from lxml import html
url = "https://www.jd.com/"
header = {
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
}
resp = requests.get(url)  # requests请求
resp.encoding='utf-8' # 不乱码
html = html.etree.HTML(resp.text)
date= html.xpath('//li[@class="cate_menu_item"]/a/text()')
print(date)
