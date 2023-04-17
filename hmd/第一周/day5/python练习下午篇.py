# -*- coding：utf-8 -*-
"""
%Author     :hmd
%FileName   :python练习下午篇.py
%Time       :2022/10/12 10:10
"""
from functools import reduce
# 手写一个函数，将str1 = “hda48465  # da4@89d8a_”作为参数传入，
# 找出整个字符串中出现次数最多的字母 输出该字母和她出现的次数
def count(str):
    c = [j for j in str if j.isalpha()]
    max =0
    dict = {}
    for i in set(c):
        a = c.count(i)
        dict[i] = a
        # print(dict)
        if a > max:
            max =a
    print(max,'我是max最大值')
    for k,v in dict.items():
        print(k,'我是键')
        print(v,'我是值v')
        if v==max:
            print(k,v)
count('hda48465#da4@89d8a_')
# def coun(str):
#     list1 = []
#     for i in str:
#         if i.isalpha():
#             list1.append(i)
#     print(list1)
#     for k in list1:
#         a = list1.count(k)
#     # for k, v in enumerate(list1):
#     #     print(list1.count(v), v)
#
#             # print(a,b)
# coun("hda48465#da4@89d8a_")
# #
'''
手写一个函数，实现五次登录机会，如果用户输入的用户名为admin，密码为admin123，
则登陆成功并终止程序，否则，登陆失败并告诉用户还有几次登陆机会
'''
# count = 0
# while (count< 5):
#     count+=tengxun
#     user = input('请输入用户名')
#     password  = input('请输入密码')
#     if user == 'admin' and password=='admin123':
#         print(f"恭喜你{count}次就登录成功")
#         break
#     else:
#         print(f"登录失败还有{5-count}次机会")
# # lambda 的使用




#  reduce 的使用
