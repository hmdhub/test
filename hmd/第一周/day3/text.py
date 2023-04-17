# -*- coding：utf-8 -*-
"""
%Author     :hmd
%FileName   :text.py
%Time       :2022/10/12 9:57
"""
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
print(zipped)  # {tengxun: 4, 2: 5, 3: 6}          # 打包为字典
#