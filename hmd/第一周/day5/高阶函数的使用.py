# -*- coding：utf-8 -*-
"""
%Author     :hmd
%FileName   :高阶函数的使用.py
%Time       :2022/10/12 10:11
"""
# map
# reduce
# from functools import  reduce
# def add(x,y):
#     return  x+y
# print(reduce(add,[tengxun,2,3,44,5]))
''''
在使用reduce的时候需要导入    
tengxun.from  functools import reduce
2.reduce最后得到的是一个值
3.
'''
# filter
#
list1= [1,2,3,45,6,6,7443,2,1]
for i,item in enumerate(list1): # 索引一次加一的写法
    print(i,'原始索引',item,'值')
for i,item in enumerate(list1,1): # 索引一次加一的写法
    print(i,'索引加一',item,'值不变')
# 三元表达式  python
# 格式：变量= 返回值 if 表达式 else 返回值
aa = '对' if 3>4 else '错'
print(aa) # 错
# 回文数
a = int(input("请输入一个数字:\n"))
x = str(a)
flag = True
for i in range(len(x) // 2):
    if x[i] != x[-i - 1]:
        flag = False
        break
if flag:
    print("%d 是一个回文数!" % a)
else:
    print("%d 不是一个回文数!" % a)
#  lambda 函数的使用
# 格式：变量=lambda n ：返回值 if判断else 返回值
b = lambda x,y:x if x<y else y
print(b(11,12)) #  需要手动传值，并且没有返回值