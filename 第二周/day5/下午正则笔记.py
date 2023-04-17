# -*- coding：utf-8 -*-
"""
%Author     :hmd
%FileName   :下午正则笔记.py
%Time       :2022/9/30 11:39
"""
import re
ret = re.match('激情\d','速度与激情10')
# print(ret)
ret1 = re.search('情','速度与激情10j激情')
# print(ret1.group(0))
ret2 = re.findall('情','速度与激情10j激情')
# print(ret)


# flag:
# 1.知道正则三个匹配方法 以及区别

# 2. 理解 \d和\d
# *: 匹配0个或无数个
# : 匹配1次过无数个
# ?: 匹配1个或0个
# .(点): 匹配任意字符

# 3.会使用re.findall() 返回的是列表

# 4.理解贪婪模式与非贪婪模式
# 贪婪(.*)：在正则中尽量往多的匹配
# 非贪婪(.*?)\：一个字符串尽量往少的匹配


s1 = '阅读量9999，点赞数1000'
a = re.findall('\d',s1)   # \d 表示匹配一个数字['9', '9', '9', '9', '1', '0', '0', '0']
# print(a)
b = re.findall('\d+',s1)
# \d+ 表示匹配多个数字['9999', '1000']
# print(b)
s2 = '阅读量9999，点赞数1000,阅读量9999，点赞数1000,阅读量9999，点赞数1000'
c = re.findall('.*',s2)  # 贪婪
# print(c)
d = re.findall('.*?',s2)  # 非贪婪
# print(d)

# 5.把一个字符串中非数字的内容拼成一个字符串
# 例如输入的是 a1b2c3----输出"abc"
h = 'a1b2c3'
# h1 = re.findall('\D',h)
h1 = re.findall('[a-zA-Z]',h)
# print(h1)
# print(''.join(h1))  # join拼接字符串




