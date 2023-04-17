""""
*_* coding: utf-8 *_*
author:蔡梦丹
time:2022/11/3 10:38
file :optMysql.PY
"""""
import  pymysql
# 导入settings 模块
from  MyMONEY import  settings
# 建立mysql 连接
sqlconnect = pymysql.connect(
    host=settings.Mysql_host,
    user = settings.Mysql_user,
    password=settings.Mysql_pwd,
    port=settings.Mysql_port,
    database=settings.Mysql_db
)
# 创建游标
cur = sqlconnect.cursor()
class Sql():
    #插入数据
    @staticmethod
    def insert_info(data):
        str = 'insert into jijin(jjit,name,qjzf,qjfh,twice,date,jz,ljjz,shouxufei,bejintime,ljjz1c,endtime,dwjz) values("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s");' % (data["jjit"], data["name"], data["qjzf"], data["qjfh"],data["twice"],data["date"],data["jz"],data["ljjz"],data["shouxufei"],data["bejintime"],data["ljjz1c"],data["endtime"], data["dwjz"])
        cur.execute(str)
        sqlconnect.commit()