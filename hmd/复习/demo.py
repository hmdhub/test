# -*- coding：utf-8 -*-
"""
%Author     :hmd
%FileName   :demo.py
%Time       :2022/11/3 14:44
"""
def get_yield():
    for i in range(5):
        yield i

def get_print():
    for i in range(5):
        print(i)

def get_return():
    res = [i for i in range(5)] # 列表推导式
    return res
print('print方法')
get_print()
result = get_return()
print('return方法')
print(result)

print('yield方法')
#第一次调用返回对象（生成器）
#需要使用next()方法取值,调用一次取一次
#也可以使用循环遍历
res = get_yield()
# print(next(res))
# print(next(res))
# print(next(res))
# print(next(res))
# print(next(res))
for i in res:
    print(i)
# print(next(res))