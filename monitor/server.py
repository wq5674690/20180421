#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import pymysql
import datetime
import time
import socket
import socketserver  # 导入socketserver模块
from datetime import datetime
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

# 格式化邮件地址
def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

# 配置邮件服务器
from_addr = "wq5674690@sina.com"
password = "qweasd5674690"
to_addr = "wq5674690@126.com"
smtp_server = "smtp.sina.com"
#---------------------------------------------------------------------------
# socket服务器端
# 创建一个类，继承自socketserver模块下的BaseRequestHandler类
class MyServer(socketserver.BaseRequestHandler):  
# 要想实现并发效果必须重写父类中的handler方法，在此方法中实现服务端的逻辑代码（不用再写连接准备，包括bind()、listen()、accept()方法）    
    def handle(self): 
        # 打开数据库连接
        db = pymysql.connect("127.0.0.1","root","root","test" )
        # db = pymysql.connect("sql12.freemysqlhosting.net","sql12175561","1K4gNWqCvy","sql12175561" )
        flag=True
        while 1:
# 下面两行代码，等于 conn,addr = socket.accept()，只不过在socketserver模块中已经替我们包装好了，还替我们包装了包括bind()、listen()、accept()方法            
            conn = self.request
            addr = self.client_address
            while 1:
                accept_data = str(conn.recv(1024), encoding="utf8")
                # 把接收的信息用下滑线分割
                str1=accept_data.split("_")
                # 把接收的字符串转化成float型数据进行判断
                cpu_1=float(str1[1])
                mem_1=float(str1[2])
                cpu_max=50
                mem_max=70
                print(accept_data)
                # 主动结束通讯
                if accept_data == "byebye":
                    break
                send_data = bytes("ok", encoding="utf8")
                conn.sendall(send_data)
                # 设置报警规则，并且把报警的内容记录到数据库中     
                if (cpu_1>cpu_max or mem_1>mem_max):
                    if (flag==True):
                        print("mail异常")
                        # 发送异常邮件
                        msg = MIMEText('您的服务器CPU或内存出现问题...', 'plain', 'utf-8')
                        msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
                        msg['To'] = _format_addr('管理员 <%s>' % to_addr)
                        msg['Subject'] = Header('这是一封报警邮件', 'utf-8').encode()
                        try:
                            server = smtplib.SMTP(smtp_server, 25)
                            server.set_debuglevel(1)
                            server.login(from_addr, password)
                            server.sendmail(from_addr, [to_addr], msg.as_string())
                            server.quit()
                            print("邮件发送成功")
                        except smtplib.SMTPException:
                            print("Error: 无法发送邮件")
                        flag=False
                    else:
                        pass
                    # 使用 cursor() 方法创建一个游标对象 cursor
                    cursor = db.cursor()
                    # 插入记录
                    sql = "INSERT INTO MONITOR(send_date_time,accept_date_time, cpu, mem) VALUES ('%s','%s','%s', '%s')" % \
                            (str1[0],datetime.now(),cpu_1, mem_1)
                    try:
                       # 执行sql语句
                       cursor.execute(sql)
                       # 执行sql语句
                       db.commit()
                    except:
                       # 发生错误时回滚
                       db.rollback()
                # elif (cpu_1==0 or mem_1==0):
                #     cursor = db.cursor()
                #     sql = "INSERT INTO MONITOR(send_date_time,accept_date_time, cpu, mem) VALUES ('%s','%s','%s', '%s')" % \
                #             (datetime.now(),datetime.now(),cpu_1, mem_1)
                #     try:
                #        # 执行sql语句
                #        cursor.execute(sql)
                #        # 执行sql语句
                #        db.commit()
                #     except:
                #        # 发生错误时回滚
                #        db.rollback()
                else:
                    if (flag==False):
                        print("mail正常")
                         # 发送恢复正常的邮件
                        msg = MIMEText('您的服务器已经在 <%s> 恢复正常' % datetime.now(), 'plain', 'utf-8')
                        msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
                        msg['To'] = _format_addr('管理员 <%s>' % to_addr)
                        msg['Subject'] = Header('这是一封报警邮件', 'utf-8').encode()
                        try:
                            server = smtplib.SMTP(smtp_server, 25)
                            server.set_debuglevel(1)
                            server.login(from_addr, password)
                            server.sendmail(from_addr, [to_addr], msg.as_string())
                            server.quit()
                            print("邮件发送成功")
                        except smtplib.SMTPException:
                            print("Error: 无法发送邮件")
                        flag=True
                    else:
                        pass
            conn.close()
        # 关闭数据库连接
        db.close()
if __name__ == '__main__':
# 传入 端口地址 和 我们新建的继承自socketserver模块下的BaseRequestHandler类  实例化对象	
    sever = socketserver.ThreadingTCPServer(("127.0.0.1", 8888),
                                            MyServer)  

# 通过调用对象的serve_forever()方法来激活服务端
    sever.serve_forever()
