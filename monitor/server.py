#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import pymysql
import datetime
import time
import socket
import socketserver  # 导入socketserver模块
from datetime import datetime
#---------------------------------------------------------------------------
# socket服务器端
# 创建一个类，继承自socketserver模块下的BaseRequestHandler类
class MyServer(socketserver.BaseRequestHandler):  
# 要想实现并发效果必须重写父类中的handler方法，在此方法中实现服务端的逻辑代码（不用再写连接准备，包括bind()、listen()、accept()方法）    
    def handle(self):  
        while 1:
# 下面两行代码，等于 conn,addr = socket.accept()，只不过在socketserver模块中已经替我们包装好了，还替我们包装了包括bind()、listen()、accept()方法            
            conn = self.request
            addr = self.client_address
            while 1:
                accept_data = str(conn.recv(1024), encoding="utf8")
                print(accept_data)
                if accept_data == "byebye":
                    break
                send_data = bytes("ok", encoding="utf8")
                conn.sendall(send_data)
            conn.close()

if __name__ == '__main__':
# 传入 端口地址 和 我们新建的继承自socketserver模块下的BaseRequestHandler类  实例化对象	
    sever = socketserver.ThreadingTCPServer(("127.0.0.1", 8888),
                                            MyServer)  

# 通过调用对象的serve_forever()方法来激活服务端
    sever.serve_forever()
#--------------------------------------------------------------------------------
# 打开数据库连接
# db = pymysql.connect("sql12.freemysqlhosting.net","sql12175561","1K4gNWqCvy","sql12175561" )
# db = pymysql.connect("127.0.0.1","root","root","test" )
# 使用 cursor() 方法创建一个游标对象 cursor
# cursor = db.cursor()

# # 使用 execute() 方法执行 SQL，如果表存在则删除
# cursor.execute("DROP TABLE IF EXISTS MONITOR")

# #创建MONITOR表  
# sql = """CREATE TABLE MONITOR (
#        id int NOT NULL,
#          date_time  DATETIME NOT NULL,
#          cpu FLOAT,
#          mem FLOAT )"""
# cursor.execute(sql)  

# #关闭数据库连接
# db.close()
#--------------------------------------------------------------------------------
# 打开数据库连接
# db = pymysql.connect("sql12.freemysqlhosting.net","sql12175561","1K4gNWqCvy","sql12175561" )
# db = pymysql.connect("127.0.0.1","root","root","test" )
# # 使用cursor()方法获取操作游标 
# cursor = db.cursor()

# # SQL 插入语句
# sql = "INSERT INTO MONITOR(id, date_time, cpu, mem) VALUES ('%d', '%s', '%s', '%s')" % \
#        (1, datetime.now(), 0.15, 0.35)
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