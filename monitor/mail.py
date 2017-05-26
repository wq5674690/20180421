#!/usr/bin/python
# -*- coding: UTF-8 -*-

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

# 邮件内容等相关信息
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
