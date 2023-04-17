# -*- coding：utf-8 -*-
"""
%Author     :hmd
%FileName   :元组练习.py
%Time       :2022/9/20 9:44
"""
# 写一个函数，实现输出公元998--2020年之间的所有闰年，要求如果闰年存在，则输出所有闰年，如果该区间不存在闰年，则输出该区间不存在闰年
# 判断闰年
# year% 4 ==0 andyear% 100 ！= 0 oryear% 400 = 0：
# 法1
def get_year():
    li = []
    for i in range(998,2021):
        if i % 4 == 0 and i % 100 != 0 or i % 400 == 0:
            li.append(i)
            print("是闰年")
        else:
            print("不是闰年")
            print(li)
            pass
        get_year()

#法2
def run(a,b):
    for i in range(a,b+1):
        if i % 100 != 0 and i % 4 == 0 or i % 400 == 0 :
            print(f"{i}是闰年")
        else:
            print(f"{i}是平年")
run(998,2020)

# 请手写一个函数，用来取出1 - 100（均包含）中3的倍数或者带有数字3的所有整数
def fun():
    list = []
    for i in range(1,101):
        if i  % 3 == 0 or i % 10 == 3:
            list.append(i)
            print(i)
fun()
#


# My_str = ‘11sdsfsdf45sfxcv67qwe_9’ 手写一个函数，计算出字符串中所有数字的和
sum = 0
my_str = '11sdsfsdf45sfxcv67qwe_9'
for i in my_str:
   if i.isdigit():
       i = int(i)
       sum += i
print(sum)




#  手写一个函数，将 ’hello xiao mi’ 作为参数输入，函数返回 ‘mi xiao hello’，注意是单词位置颠倒，而不是字母位置颠倒