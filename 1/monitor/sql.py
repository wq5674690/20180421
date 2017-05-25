#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql
from datetime import datetime

# dt=datetime.now() 
# print(dt)
# 打开数据库连接
# db = pymysql.connect("sql12.freemysqlhosting.net","sql12175561","1K4gNWqCvy","sql12175561" )
db = pymysql.connect("127.0.0.1","root","root","test" )
#---------------------------------------------------------------------------------------------
# # 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute() 方法执行 SQL，如果表存在则删除
# cursor.execute("DROP TABLE IF EXISTS MONITOR")

#创建MONITOR表  
sql = """CREATE TABLE IF NOT EXISTS MONITOR (
		 id int primary key not null auto_increment NOT NULL,
		 send_date_time  DATETIME NOT NULL,
         accept_date_time  DATETIME NOT NULL,
         cpu FLOAT,
         mem FLOAT )"""
cursor.execute(sql)  

#关闭数据库连接
db.close()
#---------------------------------------------------------------------------------------------
# 使用cursor()方法获取操作游标 
# cursor = db.cursor()

# sql = "SELECT LAST_INSERT_ID()"

# SQL 插入语句
# sql = "INSERT INTO MONITOR(date_time, cpu, mem) VALUES ('%s','%s', '%s')" % \
#        (datetime.now(), 0.268, 0.168)
# try:
#    # 执行sql语句
#    cursor.execute(sql)
#    # 执行sql语句
#    db.commit()
# except:
#    # 发生错误时回滚
#    db.rollback()

# # 关闭数据库连接
# db.close()