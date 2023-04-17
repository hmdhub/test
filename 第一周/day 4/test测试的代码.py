""""
*_* coding: utf-8 *_*
author:蔡梦丹
time:2022/9/22 15:58
file :test测试的代码.PY
"""""
lst = [1,2,3,4,5,6,7,8,9,10]
s = lst[::-1]
print(s,'第一种')
sr = lst[::1]
print(sr,'第二种')
# [10, 9, 8, 7, 6, 5, 4, 3, 2, 1] 第一种
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 第二种
string = '       123   qw'
print(len(string))
# 拿到非空格的部分
strip = string.strip()
print(strip)
a = len(strip)
print(a)
def func():
    my_str ='123.json'
    if my_str.endswith('.json'):
        my = my_str.replace('.json','.py987') # 替换
        if   not my.isspace():
            print(len(my),'非空白字符的数量')
        print(my)
func()
# 实例证明
str = "This is string example....wow!!!"
print (str.isspace())#False