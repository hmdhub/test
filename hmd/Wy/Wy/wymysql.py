# -*- coding：utf-8 -*-
"""
%Author     :hmd
%FileName   :wymysql.py
%Time       :2022/11/7 16:02
"""
from Wy import settings
import pymysql
conn = pymysql.connect(
    host=settings.Mysql_host,
    user=settings.Mysql_user,
    db=settings.Mysql_db,
    passwd=settings.Mysql_pwd,
    port=settings.Mysql_port

)

# 建立游标
cur =conn.cursor()
# 插入数据
class my():
    @staticmethod
    def insert_write(info):
        sql = 'insert into wynew(one,two,three) values ("%s","%s","%s");' % (info["cate1_name"],info["cate2_name"],info["cate3_name"])
        cur.execute(sql)
        conn.commit()