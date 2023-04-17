""""
*_* coding: utf-8 *_*
author:蔡梦丹
time:2022/9/21 18:34
file :text.PY
"""""
#  有疑问
def zi():
    dic = {}
    str = '那车水马龙的人世间,那样地来 那样地去,太匆忙'
    a = [i for i in str]
    length = len(str)
    b = [j for j in range(length)]
    # print(b)
    s = dict(zip(a, b))
    print(s,'使用zip的方法去做')
    for j in range(length):
        dic.update({str[j]:j})
    # for i in dic:
        # print(i,dic[i])
    print(dic)

    # 方法2
    for k , v in enumerate(str):
        if v =='那':
            print(k)
zi()
# zip的练习
aq = [1, 2, 3]
ba = [4, 5, 6]
ca = [4, 5, 6, 7, 8]
zipped = dict(zip(aq,ca))
print(zipped)  # {1: 4, 2: 5, 3: 6}          # 打包为字典
#