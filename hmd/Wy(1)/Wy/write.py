""""
*_* coding: utf-8 *_*
author:蔡梦丹
time:2022/11/7 16:00
file :write.PY
"""""
from Wy import settings
import pymysql
conn = pymysql.connect(database=settings.MYsql_db,
                       password=settings.MYsql_pwd,
                       host=settings.MYsql_host,
                       port=settings.MYsql_port,
                       user=settings.MYsql_user)
cur = conn.cursor()
# 插入数据
class my():
    @staticmethod
    def insert_write(info):
        sql = 'insert into newwy(one,two,three) values ("%s","%s","%s");' % (info["one"],info["two"],info["three"])
        cur.execute(sql)
        conn.commit()

    def insert_write2(info):
        sql = 'insert into newwy(name,title,price,img) values ("%s","%s","%s","%s");' % (info["name"], info["title"], info["price"],info["img"])
        cur.execute(sql)
        conn.commit()