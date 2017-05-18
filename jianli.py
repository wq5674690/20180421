#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 这是一个简历分类并把相关字段提取出来写入excel中的小工具

# 招聘网站变量：job
# 应聘人员变量：jobname
# 应聘岗位变量：post
# 应聘人员QQ变量：qq
# 其他信息变量：other

import os,sys
import shutil
import xlwt
import xlrd
from datetime import datetime

# excel样式
style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on',num_format_str='#,##0.00')
style1 = xlwt.easyxf(num_format_str='D-MMM-YY')
style2 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on')
# 创建excel工作表
wb = xlwt.Workbook()
ws = wb.add_sheet('简历信息')
# excel的固定表头信息
ws.write(1,0,"ID",style0)
ws.write(1,1,"path",style0)
ws.write(1,2,"job",style0)
ws.write(1,3,"jobname",style0)
ws.write(1,4,"post",style0)
ws.write(1,5,"qq",style0)
ws.write(1,6,"other",style0)


# 填写sheet1，A1单元格内容并赋予style0的样式
# ws.write(0, 0, array1[0], style0)
# 获取当前时间，并写入到sheet1的A2单元格并用style1样式
# ws.write(1, 0, datetime.now(), style1)

# 打开文件夹
path = "C:\demo\简历项目\demo_py1"
dirs = os.listdir( path )
path1 = "C:\demo\简历项目\demo_py"
dirs2 = os.listdir(path1)

# 输出所有文件和文件夹
for j,file in enumerate(dirs): 
	
	# print(file)
# 输出文件名，把文件以小数点分割成字符串	
	str2 = file.split(".")
# 输出小数点前的字符串，并赋值
	str3 = str2[0]
# 把小括号去掉，换成下划线
	str4 = str3.replace("(","_",1)
	str5 = str4.replace(")","",1)
# 把以下划线分割的字符串组成数组
	array1 = str5.split("_")
# 判断数组中第一个字符串是否匹配，然后复制匹配的文件到指定位置
	if array1[0]=="51job":
		shutil.copy("C:\\demo\\简历项目\\demo_py1\\"+file,"C:\\demo\\简历项目\\demo_py\\51job\\"+file)
		ws.write((j+2),1,str("C:\\demo\\简历项目\\demo_py\\51job\\"),style2)
	elif array1[0]=="智联招聘":
		shutil.copy("C:\\demo\\简历项目\\demo_py1\\"+file,"C:\\demo\\简历项目\\demo_py\\智联招聘\\"+file)
		ws.write((j+2),1,str("C:\\demo\\简历项目\\demo_py\\智联招聘\\"),style2)
	elif array1[0]=="猎豹招聘":
		shutil.copy("C:\\demo\\简历项目\\demo_py1\\"+file,"C:\\demo\\简历项目\\demo_py\\猎豹招聘\\"+file)
		ws.write((j+2),1,str("C:\\demo\\简历项目\\demo_py\\猎豹招聘\\"),style2)
	elif array1[0]=="58同城":
		shutil.copy("C:\\demo\\简历项目\\demo_py1\\"+file,"C:\\demo\\简历项目\\demo_py\\58同城\\"+file)
		ws.write((j+2),1,str("C:\\demo\\简历项目\\demo_py\\58同城\\"),style2)
	elif array1[0]=="赶集":
		shutil.copy("C:\\demo\\简历项目\\demo_py1\\"+file,"C:\\demo\\简历项目\\demo_py\\赶集\\"+file)
		ws.write((j+2),1,str("C:\\demo\\简历项目\\demo_py\\赶集\\"),style2)
	else:
		print("复制文件出错")
	# print (array1)
	for i,arr in enumerate(array1):
		# print(arr)
		ws.write((j+2),(i+2),arr,style0)
	ws.write((j+2),0,int(j),style2)
		
# for l in range(len(dirs)):
	# print(l)
	# ws.write((l+2),0,int(l),style0)
		
		

# ws.write(1,1,"asd",style0)
# 把获取到的文件名信息填写到excel中

# 保存到excel文件中
wb.save('简历统计表.xls')

 




