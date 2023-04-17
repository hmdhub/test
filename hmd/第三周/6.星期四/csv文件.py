# -*- coding：utf-8 -*-
"""
%Author     :hmd
%FileName   :csv文件.py
%Time       :2022/10/13 11:33
"""
# 导包
import csv
#tengxun.向csv文件中写入数据
# newline=''  没有空行，否则 每条数据之间有空行
with open("stu.csv",'a') as f:
    # with open("good.csv", 'a') as f:
   row3 = ['姓名', '年龄', '职业', '住址', '工资']
   row=['曹操','23','学生','黑龙江','5000']
   row2 = ['曹操2', '23', '学生', '黑龙江', '5000']
#     #写入
#     # w = csv.writer(f)
#     # w.writerow(row3)
   write=csv.writer(f)
   write.writerow(row)
print("写入完毕！")

# 2.读取
# 2.读取文件表头数据
# 方式一
with open("stu.csv") as f:
    reader = csv.reader(f)
    rows = [row for row in reader]
    # for i in rows:
    #      print(i)
    print(rows[1])

#  方式二
# with open("test.csv") as f:
# tengxun.创建阅读器对象
#     reader = csv.reader(f)
# 2.读取文件第一行数据
#     head_row = next(reader)
#     print(head_row)
#
# #tengxun.获取文件某一列数据

# with open("test.csv") as f:
#     reader = csv.reader(f)
#     column=[row for row in reader]
#     print(column[2])


# with open("test1.csv",'a+',newline='') as f:
#      row=['曹操','23','学生','黑龙江','5000']
    row2 = ['贺峻霖', '20', '学生', '重庆', '5000']
# 写入
#      write=csv.writer(f)
#      write.writerow(row2)
   # print("写入完毕！")
#      f.seek(0)
#      reader=csv.reader(f)
#      rows=[row for row in reader]
# 2.遍历rows列表
#      for row in rows:

# 3.把每一行写到Aim.csv中
#     print(row)
#     print("完毕！")


























