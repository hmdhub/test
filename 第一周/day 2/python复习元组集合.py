""""
*_* coding: utf-8 *_*
author:蔡梦丹
time:2022/9/20 9:42
file :python 复习2.PY
"""""
#  元组
a = (1,) # <class 'tuple'> # 只有一个元素的时候记得加，号
print(type(a))
b = tuple((1,3,4,3,2,1,1))#<class 'tuple'> 使用tuple函数创建
print(type(b))
print(len(b)) # 长度
print(b[1:]) #切片
c = a+b
print(c)  # 合并
#  元组检索

d = [i for i in b]
print(d,'我是循环元祖 的元素')
#  集合
f = set() # 创建空集合
ff = set([1,2,3,4]) # {1, 2, 3, 4}
fff = {1,2,3,4,5,67,22,6666,1,2} #不使用set函数创建而是使用{}直接写
print(fff,'我是用{}直接写数据的')
print(ff,'我是用set函数创建 的')
#  循环
for s in ff:
    print(s)
# 添加
ff.add('122222')
print(ff)  # {1, 2, 3, 4, '122222'}
# 删除
ff.remove(4)
print(ff) # {1, 2, 3, '122222'}
# 集合中的set 可以直接去重
q = {1,2,3,2.2,2,4,4,44,3,5,6,6}
print(set(q),'我是集合但是我会去重')
# 集合推导式
set = {
    x for x in (2, 3, 4, 1, 2, 1)
}
print(set,type(set))  #{1, 2, 3, 4} <class 'set'>