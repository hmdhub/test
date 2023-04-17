# -*- coding：utf-8 -*-
"""
%Author     :hmd
%FileName   :optMysql.py
%Time       :2022/11/3 11:40
"""
import pymysql
# 导入settings模块
from mySpiders import settings

# 建立mysql连接
sqlConnect = pymysql.connect(
    host=settings.Mysql_host,
    user=settings.Mysql_user,
    passwd=settings.Mysql_pwd,
    db=settings.Mysql_db,
    port=settings.Mysql_port
)
# 建立游标
cur = sqlConnect.cursor()


# 类
class Sql():
    # 创建表（create）
    @staticmethod
    def create_table():
        str = 'CREATE TABLE chinaz(id int auto_increment PRIMARY KEY,uname VARCHAR (255),info VARCHAR (255),rank VARCHAR (255));'
        cur.execute(str)  # 用游标执行sql语句
        sqlConnect.commit()  # 提交
        pass

    #  插入数据（insert）
    @staticmethod
    def insert_chinaz(data):  # data 是形参
        # sql语句
        str = 'insert into chinaz(uname,info,rank)values("%s","%s","%s");' % (data["name"], data["info"], data["rank"])
        cur.execute(str)
        sqlConnect.commit()
        pass

    # 更新数据（updata）
    @staticmethod
    def update_chinaz(s):
        # name = input("请输入您要修改的名字")
        # info = input("请输入您要修改的信息")
        # rank = input("请输入您要修改的排名")
        sql = f'update chinaz set uname={s},rank = {rank} where id = 1'
        cur.execute(sql)
        sqlConnect.commit()
        pass

    # 删除数据（delete）
    @staticmethod
    def delete_chinaz():
        pass

    # 关闭连接 (close)
    @staticmethod
    def close_chinaz():
        pass

    def aa(self):
        pass

    pass
