""""
*_* coding: utf-8 *_*
author:蔡梦丹
time:2022/9/29 11:30
file :下午课堂笔记.PY
"""""
from lxml import html

doc = '''' 
<div>
    <ul>
        <li class="item-0">
            <a href="link1.html">first item</a>
            <a href="link1.html">1</a>   
            <a href="link1.html">2</a>
            <a href="link1.html">3</a>
                 
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
# contains() 函数:（包含）属性不加引号
html = html.etree.HTML(doc)
first = html.xpath('//*[contains(@class,"item")]/a/text()')
# print(first)
# starts-with()函数匹配以......开头:
second = html.xpath('//*[starts-with(@class,"item-1")]/a/text()')
# print(second)  # ['second item', 'fourth item']
# position()位置函数
third = html.xpath('//li[@class="item-0"]/a[@href="link1.html"][position()<2]/text()') # 正确的格式
print(third)