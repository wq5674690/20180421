#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import psutil
import datetime
import socket

#-------------------------------------------------------------------
# socket客户端
sk = socket.socket()
sk.connect(("127.0.0.1", 8888))  # 主动初始化与服务器端的连接
while True:
    send_data = input("输入发送内容:")
    sk.sendall(bytes(send_data, encoding="utf8"))
    if send_data == "byebye":
        break
    accept_data = str(sk.recv(1024), encoding="utf8")
    print("".join(("接收内容：", accept_data)))
sk.close()

#--------------------------------------------------------------------
# 查询agent服务器状态

# check CPU
# 查看cpu所有信息
psutil.cpu_times()
# 显示cpu所有逻辑信息
psutil.cpu_times(percpu=True)
# 查看用户的cpu时间比
psutil.cpu_times().user
# 查看cpu逻辑个数
psutil.cpu_count()
# 查看cpu物理个数
psutil.cpu_count(logical=False)


# check memory
mem = psutil.virtual_memory()
# 系统内存的所有信息
mem
# 系统总计内存
mem.total
# 系统已经使用内存
mem.used
# 系统空闲内存
mem.free
# 获取swap内存信息
psutil.swap_memory()

# check disk
# 磁盘利用率
psutil.disk_usage()
'''
磁盘IO信息包括read_count(读IO数)，write_count(写IO数)
read_bytes(IO写字节数)，read_time(磁盘读时间)，write_time(磁盘写时间)
'''
# IO信息
psutil.disk_io_counters()
# 获取磁盘的完整信息
psutil.disk_partitions()
# 获取分区表的参数
psutil.disk_usage('/')   #获取/分区的状态
# 获取硬盘IO总个数
psutil.disk_io_counters()
# 获取单个分区IO个数
psutil.disk_io_counters(perdisk=True)    #perdisk=True参数获取单个分区IO个数
# 读取网络信息
'''
	网络信息与磁盘IO信息类似,涉及到几个关键点，包括byes_sent(发送字节数),byte_recv=xxx(接受字节数),
pack-ets_sent=xxx(发送字节数),pack-ets_recv=xxx(接收数据包数)
'''
# 获取网络总IO信息
psutil.net_io_counters()
# 输出网络每个接口信息
psutil.net_io_counters(pernic=True)     #pernic=True

# 获取当前系统用户登录信息
psutil.users()
# 获取开机时间
psutil.boot_time() #以Linux时间格式返回
datetime.datetime.fromtimestamp(psutil.boot_time ()).strftime("%Y-%m-%d %H: %M: %S") #转换成自然时间格式

# 系统进程管理
'''
	获取当前系统的进程信息,获取当前程序的运行状态,包括进程的启动时间,查看设置CPU亲和度,内存使用率,IO信息
socket连接,线程数等
获取进程信息
'''
# 查看系统全部进程
psutil.pids()
# 查看单个进程
p = psutil.Process(2423) 
p.name()   #进程名
p.exe()    #进程的bin路径
p.cwd()    #进程的工作目录绝对路径
p.status()   #进程状态
p.create_time()  #进程创建时间
p.uids()    #进程uid信息
p.gids()    #进程的gid信息
p.cpu_times()   #进程的cpu时间信息,包括user,system两个cpu信息
p.cpu_affinity()  #get进程cpu亲和度,如果要设置cpu亲和度,将cpu号作为参考就好
p.memory_percent()  #进程内存利用率
p.memory_info()    #进程内存rss,vms信息
p.io_counters()    #进程的IO信息,包括读写IO数字及参数
p.connectios()   #返回进程列表
p.num_threads()  #进程开启的线程数
听过psutil的Popen方法启动应用程序，可以跟踪程序的相关信息
from subprocess import PIPE
p = psutil.Popen(["/usr/bin/python", "-c", "print('hello')"],stdout=PIPE)
p.name()
p.username()
#------------------------------------------------------------------------