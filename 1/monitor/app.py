#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import psutil
import datetime
import socket
import time
import os
from datetime import datetime

cpu = {'user' : 0, 'system' : 0, 'idle' : 0, 'percent' : 0}  
mem = {'total' : 0, 'avaiable' : 0, 'percent' : 0, 'used' : 0, 'free' : 0}  
  
#磁盘名称  
disk_id = []  
#将每个磁盘的total used free percent 分别存入到相应的list  
disk_total = []  
disk_used = []  
disk_free = []  
disk_percent = []  
  
#获取CPU信息  
def get_cpu_info():  
    cpu_times = psutil.cpu_times()  
    cpu['user'] = cpu_times.user  
    cpu['system'] = cpu_times.system  
    cpu['idle'] = cpu_times.idle  
    cpu['percent'] = psutil.cpu_percent(interval=2)  
#获取内存信息  
def get_mem_info():  
    mem_info = psutil.virtual_memory()  
    mem['total'] = mem_info.total  
    mem['available'] = mem_info.available  
    mem['percent'] = mem_info.percent  
    mem['used'] = mem_info.used  
    mem['free'] = mem_info.free  
#获取磁盘  
def get_disk_info():  
    for id in psutil.disk_partitions():  
        if 'cdrom' in id.opts or id.fstype == '':  
            continue  
        disk_name = id.device.split(':')  
        s = disk_name[0]  
        disk_id.append(s)  
        disk_info = psutil.disk_usage(id.device)  
        disk_total.append(disk_info.total)  
        disk_used.append(disk_info.used)  
        disk_free.append(disk_info.free)  
        disk_percent.append(disk_info.percent)  
            
# mem_status = mem['percent']
# get_disk_info()
# for i in range(len(disk_id)):  
# 	print (u'%s盘空闲率: %s %%' % (disk_id[i],100 - disk_percent[i]))
# 	
def sleepTime(hour,min,sec):
	return (hour*3600 + min*60 + sec)
# 在设定频率时，需要把时间加2秒钟，才为实际频率时间
second = sleepTime(0,0,5)

# socket客户端
# 主动初始化与服务器端的连接
sk = socket.socket()
sk.connect(("127.0.0.1", 8888))
while True:
    get_cpu_info()
    get_mem_info()
    # get_disk_info()
    # arr=0
    # for i in range(len(disk_id)):  
    #     arr=(u'%s盘空闲率: %s %%' % (disk_id[i],100 - disk_percent[i]))
    #     print(arr)
    send_data =  (u"%s_%s_%s" % (datetime.now(),cpu['percent'],mem['percent']))
    sk.sendall(bytes(send_data, encoding="utf8"))
    # 间隔5秒钟执行一次
    time.sleep(second)
    if send_data == "byebye":
        break
    accept_data = str(sk.recv(1024), encoding="utf8")
    print("".join(("接收内容：", accept_data)))
sk.close()
