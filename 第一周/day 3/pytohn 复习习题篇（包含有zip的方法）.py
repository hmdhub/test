""""
*_* coding: utf-8 *_*
author:蔡梦丹
time:2022/9/21 15:28
file :pytohn 复习.PY
"""""
''''
问题归纳
1.闰年的判断方法   能被4整除不能被100整除或者能被400真除
2.i % 10 == 3 or i //10==3个位含3十位含3 或者使用 '3' in str(i)
3.巧妙的用列表推导式简单的写
4.字符串的join方法可以用；在python的列表中循环会取所有的结果但是如果想把他们拼接在一起的话可以使用join 进行拼接即可
5.如果在一个字符串中同是出现多个相同的子字符串，想要找到最后一个的子字符串的下标可以使用rfind(找不到会返回-1) 和rindex（找不到会报错）
6.zip的话可以将两个序列转化为一个序列很好用
'''
# 1.判断闰年写一个函数，实现输出公元998--2020年之间的所有闰年，要求如果闰年存在，则输出所有闰年，如果该区间不存在闰年，则输出该区间不存在闰年。
def fun(a, b):
    list1 = []
    for k in range(a,b): # range(前取后不取)
        if k % 4 == 0 and k % 100 != 0 or k % 400 == 0: # 注意闰年的判断方法
            list1.append(k)
        else:
            print(k,"我不是闰年")
    print(list1,'区间内所有闰年')
fun(998,2021)
#2.请手写一个函数，用来取出1-100（均包含）中3的倍数或者带有数字3的所有整数
##  方法1
def functi(a, b):
    list2 = []
    for i in range(a, b):
        if i % 3 == 0 or (i % 10 == 3 or i //10==3):
            list2.append(i)
    print(list2)
functi(1, 101)
# 方法2
def  functi(a,b):
    for i in range(a,b):
        if i % 3 ==0 or '3' in str(i):
            print(i)
functi(1,101)
#3.My_str = ‘11sdsfsdf45sfxcv67qwe_9’ 手写一个函数，计算出字符串中所有数字的和  结果为33
My_str = '11sdsfsdf45sfxcv67qwe_9'
list3 = []
def ma():
    for i in My_str:
        if i.isdigit():
                list3.append(i)
    su = sum([int(i) for i in list3])
    print(su)
ma()
# 4.手写一个函数，将 ’hello xiao mi’ 作为参数输入，函数返回 ‘mi xiao hello’，注意是单词位置颠倒，而不是字母位置颠倒
def nn(c):
        cc=c.split(' ') # ['hello', 'xiao', 'mi']
        cc.reverse()
        print(" ".join(cc))

nn('hello xiao mi')
#5.str = '那车水马龙的人世间,那样地来 那样地去,太匆忙' 写一个函数，输出最后一次出现"那"的下标
# 方法1
str = '那车水马龙的人世间,那样地来 那样地去,太匆忙'
def a():
    print(str.rindex('那'), '我是最后一个下标"那"')# 方法一实现
    print(str.rfind('那'))  # 15  # 方法二实现
a()
# 方法三
for k, v in enumerate(str):
    if v == '那':
        print(k)
# 第四种
def zi():
    dic = {}
    str = '那车水马龙的人世间,那样地来 那样地去,太匆忙'
    aa = len(str)
    a = [i for i in str]
    b = [b for b in range(aa)]
    s = dict(zip(a, b))
    for k, v in s.items():
        if k == "那":
            print(v, '我是那')
    print(s)
    # print(a,b)
zi()