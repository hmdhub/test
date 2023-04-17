""""
*_* coding: utf-8 *_*
author:蔡梦丹
time:2022/9/29 11:31
file :下午课堂练习.PY
"""""
import requests
from lxml import html
# 目的：使用xpath获取html中想要的信息
# 1.得要一个网页的响应内容 response.text 字符串
# 三个引号表示什么？注释 或者是可以换行的字符串
doc = '''' 
<div>
    <ul>
        <li class="item-0">
            <a href="link1.html">first item</a>
        </li>
        <li class="item-1">
            <a href="link2.html">second item</a>
        </li>
        <li class="item-inactive">
            <a href="link3.html">third item</a>
        </li>
        <li class="item-1">
            <a href="link4.html">fourth item</a>
        </li>
        <li class="item-0">
            <a href="link5.html">fifth item</a> 
        </li> 
    </ul>
 </div>
'''
# 3.将响应的内容转化为文档树对象
info = html.etree.HTML(doc)
# 4. 使用xpath  结果均为list类型的数据
# 获取任意的 li 标签方法
a = info.xpath('//li')  # 获取任意的li 标签
b = info.xpath('//div/ul/li')  # 获取任意的li标签
# print(a)
# print(b)
# 获取任意的a标签
c = info.xpath('//div/ul/li/a')
c1 = info.xpath('//a')
c2 = info.xpath('//li/a')
# 获取任意a标签的href 值
bb = info.xpath('//a[@href]/text()') # [<Element a at 0x1c5869ced48>
# print(bb)
b3 = info.xpath('//a/@href')  # ['link1.html'
# print(b3)
# 获取任意的li标签的class 属性
d = info.xpath('//li/@class')
# 获取任意的a标签的文字信息
e = info.xpath('//a/text()')
# 获取第一个a 标签的文字信息
f = info.xpath('//li[1]/a/text()')
ff = info.xpath('//li/a/text()')[0]
# 或者使用列表的方法
aa = e[0]
# 获取最后一个a 标签的文字信息
b5 = e[-1]
gg = info.xpath('//li/a/text()')[-1]
g = info.xpath('//li[last()]/a/text()')
# 获取class = item-0 的li标签下的a标签的href 属性
ss = info.xpath('//li[@class="item-0"]/a/@href')
# print(ss)
# contains 包含 属性是不加引号
d2 = info.xpath()