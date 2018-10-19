#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
import sys
import traceback
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

def send_mail_attach(send_content,file_path,file_name):
    smtp_server = "smtp.139.com"
    user = "15914531973@139.com"
    password = "gmcc13579"
    # password = "ysnyuxasgcgrcigi"

    receiver = "15812421301@139.com"
    sender = "15914531973@139.com"

    subject = "kqi数据监控"
    content = '<html><h4 style="color:blue">'+send_content+'</h4></html>'
    # msg = MIMEText(content, "html", "utf-8")
    msg = MIMEMultipart()
    msg["Subject"] = Header(subject, "utf-8")
    msg["From"] = sender
    msg["To"] = receiver

    # 邮件正文内容
    msg.attach(MIMEText(content, 'html', 'utf-8'))

    # 构造附件1，传送当前目录下的 test.txt 文件
    att1 = MIMEText(open(file_path, 'rb').read(), 'base64', 'utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    att1["Content-Disposition"] = 'attachment; filename="'+file_name+'"'
    msg.attach(att1)
    smtp = smtplib.SMTP_SSL(smtp_server, 465)
    smtp.helo(smtp_server)
    smtp.ehlo(smtp_server)
    smtp.login(user, password)
    print("开始发邮件")
    try:
        smtp.sendmail(sender, receiver, msg.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        traceback.print_exception(exc_type, exc_value, exc_traceback)
        print("Error: 无法发送邮件")

if __name__=="__main__":
    send_mail_attach("下载异常","E:\\unlogin.png",'unlogin.png')