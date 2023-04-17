# -*- coding：utf-8 -*-
"""
%Author     :hmd
%FileName   :txmysql.py
%Time       :2022/11/3 14:15
"""
import pymysql
# 导入settings模块
from Mytengxun import settings
# 建立mysql连接
sqlConnect = pymysql.connect(
    host = settings.Mysql_host,
    user = settings.Mysql_user,
    passwd = settings.Mysql_pwd,
    db = settings.Mysql_db,
    port = settings.Mysql_port
)

# 建立游标
cur = sqlConnect.cursor()
class Sql():
    # 创建表 （create）
    @staticmethod
    def create_table():
        str = 'CREATE TABLE teng(id int auto_increment PRIMARY KEY,uname VARCHAR (255),class_link VARCHAR (255))'
        cur.execute(str)
        sqlConnect.commit()
        pass
    # 插入数据 （insert）
    @staticmethod
    def insert_teng(data):
        str = f'insert into teng(uname,class_link) values("%s","%s");' % (data["name"],data["class_link"])
        cur.execute(str)
        sqlConnect.commit()
        pass
