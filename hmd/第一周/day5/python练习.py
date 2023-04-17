# -*- coding：utf-8 -*-
"""
%Author     :hmd
%FileName   :python练习.py
%Time       :2022/10/12 10:01
"""
import random
'''''
问题归纳
tengxun.如果变循环边删除会出现漏删的情况如果到这删就不会出现类似的情况/或者采用去重的思想也可以实现
2.r+ 可以读也可以写不需要移动光标。但是w+和a+ 操作完写之后需要读的话需要移动光标seek(0)
3.高阶函数在最后的时候是一个迭代器可以使用for循环将结果遍历出来，或者直接强转成你想要的序列例如print(list(new)) # # ['王二'] 可以直接强转为列表也可以
4.range（包含，不包含）     random.randint(包含，包含)
5.高阶函数 map reduce filter 和匿名函数。注意区别    还有就是map可以和lambda一起使用效果杠杠的

'''
# 第一题： 请手写一个函数，创建一个空列表alist，使用随机数模块随机生成10个整数，数字范围在[11-111] 这个区间，
#  并将生成的10个随机数全部添加到alist中，添加完成后，求输出所有随机数之和。
def math():
    alist = []
    for i in range(10):
        a = random.randint(11,111)
        i =a
        alist.append(i)
    b = sum(alist)
    print(b,'所有随机数的和')
    print(alist,'所有的随机数')
math()
#  第二题 怎么将列表[tengxun,2,3,4]变成[2,3,4,5]
a = [1,2,3,4]
b = []
c = []
# [2,3,4,5]
# # 方法1
for i in a[1:]:
    b.append(i)
b.append(5)
print(b) # [2, 3, 4, 5]
# # 方法2
for i in a:
    i =i+1
    c.append(i)
print(c) #[2, 3, 4, 5]
#  第三种
cc = [i+1 for i in range(1,5) if i<i+1]
print(cc) # [2, 3, 4, 5]
# # 第四种 map函数
def mm(x):
    return x+1
aa = [1,2,3,4]
bb= []
for i in map(mm,aa):
    print(i,end=' ')
    bb.append(i)
    print(bb)
# 第四种 map和lambada结合
def four():
    a = [1,2,3,4]
    b = []
    # 1遍历
    for i in a:
        b.append(i+1)
    # 2列表推导式
    c = [j+1 for j in a]
    # 3 map 函数 lambad 匿名函数
    d= map(lambda k : k+1,a)
    print(d) # <map object at 0x00000192CD3E7780>
    print(list(d))
four()


#  第三题 请写一个函数，实现向“test.txt”文件中写入两行数据，第一行写入数据“hello world”，第二行写入“hello python”
def ww():
    with open('test.txt', mode='r+', encoding='utf-8') as f:
        f.write('hello world\nhello python')
        a =f.readlines()
        print(a)
    f.close()
ww()
#  方法2 w+实现
def w():
    with open('test.txt', mode='w+', encoding='utf-8') as f:
        f.write('hello world\nhello python')
        f.seek(0)
        a =f.readlines()
        print(a,'使用w+的实现读写注意看区别')
    f.close()
w()
# 第三题的扩展   读取数据 请写一个函数，实现向“test.txt”文件中写入两行数据，
# 第一行写入数据“hello world”，第二行写入“hello python”
with open('test.txt',mode='r',encoding='utf-8') as f:
    a =f.read()
    print(a)
    f.close()
# a = [“张三”,”张四”,”张五”,”王二”] 如何删除姓张的
a = ['张三', '张四', '张五', '王二']
def fi():
    for q in a[::-1]:
            # if q in str('张'):
            if q[0] == '张':
                a.remove(q)
fi()
print(list((filter(fi(),a))))
# 方法2  使用列表去重的方法去写这个
list2 = []
for i in a:
    for q in i:
        if q in str('张'):
            list2.append(i)
print(list2)
for z in list2[::-1]:
    a.remove(z)
print(a)
# 方法3
def fun8(b):
    return  b[0]!='张'
print(filter(fun8,a)) #<filter object at 0x00000235C3CD7898>
new = filter(fun8,a) # ['王二']
# 如果强转为列表就不需要for 循环了，二者选其一既可以
# for i in new:
#     print(i)
print(list(new)) # # ['王二'] 可以直接强转为列表也可以