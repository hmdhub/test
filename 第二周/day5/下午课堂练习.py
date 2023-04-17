""""
*_* coding: utf-8 *_*
author:蔡梦丹
time:2022/9/30 9:45
file :下午课堂练习.PY
"""""
# 慧聪网练习xpath
import  re
import  requests
from lxml import  html
# # 5.把一个字符串中非数字的内容拼成一个字符串
# # 例如输入的是 a1b2c3----输出"abc"
a = 'a1b2c3'
b = re.findall('\D+',a)
# print(b)
c = "".join(b)
# print(c)
url = 'https://www.hc360.com/'
header = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}
resp =requests.get(url,headers= header)
resp.encoding = 'utf-8'
# print(resp.text)
html1 = html.etree.HTML(resp.text)
# 一级目录
dd = html1.xpath('//dt[@class="sub-menu-dt"]/span/text()')
print(dd)
# # 二级大目录
# s = html1.xpath('//dd[@class="sub-menu-dd"]/dl/dt/text()')
# print(s)
# # 二级中目录
# popo = html1.xpath('//dd[@class="sub-menu-dd"]/dl//a/text()')
# print(popo)
# 上述内容会出现不对版的额情况
for i in dd:
    dict = {}
    s = html1.xpath('//dd[@class="sub-menu-dd"]/dl/dt/text()')
    popo = html1.xpath('//dd[@class="sub-menu-dd"]/dl//a/text()')
    dict[i] = s
    dict[s] = popo
    print(dict)