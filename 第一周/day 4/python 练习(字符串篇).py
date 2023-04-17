""""
*_* coding: utf-8 *_*
author:蔡梦丹
time:2022/9/22 13:35
file :练习.PY
"""""
import re
'''''
1.回文数既可以使用% 或者// 也可以使用字符串的切片操作让其相等
2.非空白字符数量  '   123  ' 第一种方法就是isspace()直接计算空白字符的数量(返回结果为布尔值)看是否只包含空格。
或者就是strip.去除左右两端的空格 用原来的长度-strip的部分就是=非空白字符的数量
3.re 在正则匹配是122lllll 如果我想要匹配所有的数字 直接\d 即可在for循环里面
4.repalce('old','new') 别写反了


'''
#  1.回文数
# 方法 1
'''
写一个函数，实现判断100 - 150之间是否存在回文数，
如果存在输出全部回文数及其数量，如果不存在，
则输出该区间不存在回文数（回文数：正着读和反着读相同的数例如：171 / 181）
'''
def ma(a, b):
    list1 = []
    for i in range(a, b):
        if (i // 100 % 10 == i// 10 % 10) and (i // 1000 == i % 10):
            list1.append(i)
    print(list1)
ma(1000, 1500)
# 回文数 方法2
def fun5():
    sum = 0
    for i in range(1000,13000):
        if str(i)==str(i)[::-1]:
            print(i,end=' ')
            sum+=1
        if sum == 0:
            print("没有回文数")
    print(sum)
fun5()
# 2.题目'my_str=‘123.json’ 写一个函数，判断字符串是否以”.json”结束,如果是以”.json”,要求将“.json”替换为“.py987”''，并输出my_str中非空白字符数量'
def func():
    my_str ='123.json'
    if my_str.endswith('.json'):
        my = my_str.replace('.json','.py987') # 替换
        if  not my.isspace():
            print(len(my),'非空白字符的数量')
            print(my)
func()
'''''
str = '    ws    hiweuh       fewuf       '
s = str.isspace()  # False
print(s)
st2 = '                '
print(st2.isspace()) # True
'''''
# 3.请手写一个函数，某个字符串为“abc102324123499123ABC”，计算该字符串中所有数字之和以及字母的数量
def ma():
    #  方法一
    sum = 0
    list1 = []
    a = 'abc102324123499123ABC'
    for i in a:
        if i.isdigit():
            i = int(i)
            sum += i
        elif i.isalpha():
            list1.append(i)
    print(sum, len(list1))


ma()
def am():
# 方法二 正则
    a = 'abc102324123499123ABC'
    sum = 0
    pattern = re.compile(r'\d')  # ['102324123499123'] + 的意思就是说匹配前面的字符一次或者多次。但是这个字符串压根没必要。
    pattern2 = re.compile(r'[a-zA-Z]')
    obj = pattern2.findall(a)
    obj2 = pattern.findall(a)
    print(len(obj), "得到的是字符串中字母的数量")
    print(obj2)
    for i in obj2:
        i = int(i)
        sum += i  # 类型转换
    print(sum, len(obj), "得到的是字符串中字母的数量")
am()
