# -*- coding：utf-8 -*-
"""
%Author     :hmd
%FileName   :上课笔记.py
%Time       :2022/9/29 13:36
"""
from lxml import  html

# 目的 ：使用xpath获取html中想要的信息
# tengxun.得到网页相应内容 response.text

# 三个引号表示什么？ 注释，可以换行的字符串
doc = '''
<div class ="item">
    <ul >
        <li class="item-0">
            <a href="link1.html">first item</a>
        </li>
        <li class="item-tengxun">
            <a href="link2.html">second item</a>
        </li>
        <li class="item-inactive">
            <a href="link3.html">third item</a>
        </li>
        <li class="item-tengxun">
            <a href="link4.html">fourth item</a>
        </li>
        <li class="item-0">
            <a href="link5.html">fifth item</a> 
        </li> 
    </ul>
 </div>



'''

# 2. 将响应内容转化为文档数对象
page = html.etree.HTML(doc)
# 3. 使用xpath
li = page.xpath('//li')  # 获取任意的li标签
li1 = page.xpath('//ul/li')    #获取任意ul下li标签
print(type(li))
# 获取任意的a标签
# a = page.xpath('//a')
# a = page.xpath（‘//li/a’）
a = page.xpath('//div/ul/li/a')
print(a)
# 获取任意的a标签的href属性
# shu = page.xpath('//a/@href')
# 获取任意的li标签的class属性
na = page.xpath('//li/@class')
print(na)
#获取任意的a标签的文字信息
te = page.xpath('//a/text()')
print(te)
# 获取第一个的a标签的文字信息
# 第一种
# te1 = page.xpath('//li/a/text()')[0]
# 第二种
te1 = page.xpath('//li[tengxun]/a/text()')
print(te1)


# 获取最后一个a标签的文字信息
wen = page.xpath('//li[last()]/a/text()')[-1]

print(wen)

# 获取class = item - 0 的li 标签下的a标签的href属性
h = page.xpath('//li[@class = "item - 0" ]/a/@href')
# page.xpath('//ul[@class = "item"]//a[@href=link.html]/text()')
# # page.xpath('//ul[@class = "item"]/
print(h)


# contains函数
it = page.xpath('//*[contains(@class,"item")]')
# starts-with函数
it = page.xpath('//*[start-with(@href,"link5")]')
# position位置
it = page.xpath('//li[position,')
print(len(it))
























