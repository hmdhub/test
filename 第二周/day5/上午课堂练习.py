""""
*_* coding: utf-8 *_*
author:蔡梦丹
time:2022/9/30 9:45
file :上午课堂练习.PY
"""""
import  re
str = '蔡梦丹今年20岁'
s = re.match('蔡梦丹今年\d',str)
print(s.group(0))
ss = re.match('\d蔡梦丹今年\d',str)
print(ss)   #如果打印的时候不打印group()的部分没有匹配到的话就是None，加了group就是报错