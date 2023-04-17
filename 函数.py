# -*- coding：utf-8 -*-
"""
%Author     :hmd
%FileName   :函数.py
%Time       :2023/2/21 16:38
"""
# 一.任意两个数字的和
# 1.方法一
def a(x,y):
    b = x+y
    print(b)
# a(19,28)
# 查看文档
help(a)  # 放函数名字不需要调用（函数名不加小括号）

# 2.方法二：在控制台输出数字的和
def score():
    a = int(input("请输入数字:"))
    b = int(input("请输入数字:"))
    c = a+b
    print(c)
    return()
score()
# 判断：是数字就求和，不是数字就拼接
def score():
    a = int(input("请输入数字:"))
    b = int(input("请输入数字:"))
    if a.isdigit()and b.isdigit():
        s = int(a) + int(b)
        print(s)
    else:
        print(f"输入数据有误{a}{b}")
# score()
help(a)  # 放函数名字不需要调用（函数名不加小括号）

# 二、函数的文档说明
# 作用：保存函数解释说明的信息
# 语法：
# 	def 函数名(参数)：
#     	""" 说明文档的位置 """
#         代码
#         ......


# 三、函数作用：封装代码，高效的代码重用

# 四、函数嵌套调用执行顺序
#自定义函数testB
def testB():
    print('---- testB start ----')
    print('这里是testB函数执行的代码...(省略)...')
    print('---- testB end ----')
#自定义函数testA
def testA():
    print('---- testA start ----')
    testB()
    print('---- testA end ----')
testA()
#结果如下：
# ---- testA start ----
# ---- testB start ----
# 这里是testB函数执行的代码...(省略)...
# ---- testB end ----
# ---- testA end ----
#
# 五、函数嵌套调用执行流顺序
# 1.自定义函数只有在函数被调用时，函数才会执行
# 2.如果函数A中，调用了另一个函数B，那么先把函数B中的任务都执行完毕之后才会回到上次函数A执行的位置