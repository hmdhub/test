""""
*_* coding: utf-8 *_*
author:蔡梦丹
time:2022/9/30 9:45
file :下午课堂笔记.PY
"""""
import  re
#\d 和 \d+ 的区别
s1 = '阅读量9999，点赞量1111'
a = re.findall('\d',s1)
print(a)
b = re.findall('\d+',s1)
print(b)
s2 = '速度与激情速度与激情速度与激情速度与激情速度与激情速度与激情速度与激情'
c = re.findall('.*?情',s2)
print(c)
d = re.findall('.*情',s2)
print(d)