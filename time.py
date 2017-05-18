#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 这是一个统计通话时长的小工具，导入特定的表格，抓取数据然后进行简单的处理
import os,sys
import shutil
import xlwt
import xlrd
from datetime import datetime

# excel样式
style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on',num_format_str='#,##0.00')
style1 = xlwt.easyxf(num_format_str='HH:MM:SS')
style2 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on')
style3 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on',num_format_str='#,##0.00')
style4 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on',num_format_str='#,##0.00')
style5 = xlwt.easyxf(num_format_str='YYYY-MM-RR')
#设置单元格宽度
# col.width=256*16

# 创建excel工作表
wb = xlwt.Workbook()
ws = wb.add_sheet('统计详情')

# 读取excel
data = xlrd.open_workbook(r'c:\demo\time\20170417_原始数据.xlsx')
#通过名称获取
table = data.sheet_by_name(u'Sheet4') 

# 获取行数和列数
nrows = table.nrows
ncols = table.ncols

# 设置行宽
for w in range(16,25):
	ws.col(w).width=256*16 # 256代表一个字符的长度，16代表几个字符

# excel的固定表头信息
ws.write(1,17,"猛龙队（罗斌）",style0)
ws.write(1,18,"先锋队（冯伟军）",style0)
ws.write(1,19,"启航队（胡来）",style0)
ws.write(1,20,"猎豹队（郭瑞）",style0)
ws.write(1,21,"雄风队（楚枫）",style0)
ws.write(1,22,"飞鹰队（田丰平）",style0)
ws.write(1,23,"超越队（王悦）",style0)
ws.write(1,24,"进攻队（孙亚伟）",style0)

ws.write(2,16,"呼出总时长",style0)
ws.write(3,16,"最高通话时长",style0)
ws.write(4,16,"最高通话人员",style0)
ws.write(5,16,"拨打人数(人)",style0)
ws.write(6,16,"平均时长",style0)

ws.write(8,22,"记录时间：")
ws.write(9,22,"核对时间：")

# 返回数据到excel
for i in range(0,nrows):
	for j in range(0,ncols):
		ws.write(i,j,str(table.cell(i,j).value))
		#table.cell(i,j).value #单元格的值'
		
# 写入数据
for j in range(0,8):
	#输出总时长
	sumtime=0
	arr1=[] #创建一个数组
	obj={}
	for i in range(10+j*20,29+j*20):
		time1=table.cell(i,9).value
		if time1>0:
			arr1.append(time1) #把大于0的放入数组中
		# print(arr)
		sumtime+=time1
		obj[i]=time1
		max1=max(obj.items(),key=lambda x:x[1]) #每个字典的最大值
		#continue
	# print('时长最高人员:',str(table.cell(max1[0],1).value)) #时长最高人员
	ws.write(4,17+j,str(table.cell(max1[0],1).value))
	# print('总时长：',sumtime) #总时长
	ws.write(2,17+j,sumtime,style1)
	# print('最高时长:',max(arr1)) #最高时长
	ws.write(3,17+j,max(arr1),style1)
	# print('拨打人数:',len(arr1)) #拨打人数
	ws.write(5,17+j,len(arr1))
	# print('平均时长:',sumtime/len(arr1)) #平均时长
	ws.write(6,17+j,sumtime/len(arr1),style1)

str1=str(table.cell(2,1).value)
#print(str1.split('至')[0])
ws.write(8,23,str1.split('至')[0]) #把str1字符串从‘至’开始分割成二个，只去第一个
str2=str(datetime.now())
ws.write(9,23,str2.split()[0],style5)

# 设置居中
# ws is worksheet
# myCell=ws.cell('A1')
# myCell.style.alignment.vertical=Alignment.VERTICAL_MIDDLE
				
		
# 保存到excel文件中
wb.save('20170417_核对数据.xls')
