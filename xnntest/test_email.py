import smtplib
import sys
import traceback
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header

smtp_server = "smtp.139.com"
user = "15914531973@139.com"
password = "gmcc13579"
# password = "ysnyuxasgcgrcigi"

receiver= "15812421301@139.com"
sender="15914531973@139.com"

subject="kqi数据监控"
content = '<html><h1 style="color:red">python测试邮件</h></html>'
msg = MIMEText(content, "html", "utf-8")
# msg = MIMEMultipart()
msg["Subject"]=Header(subject,"utf-8")
msg["From"] = sender
msg["To"] = receiver

smtp = smtplib.SMTP_SSL(smtp_server, 465)
smtp.helo(smtp_server)
smtp.ehlo(smtp_server)
smtp.login(user,password)
print("开始发邮件")
try:
    smtp.sendmail(sender, receiver, msg.as_string())
    print("邮件发送成功")
except smtplib.SMTPException:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    traceback.print_exception(exc_type, exc_value, exc_traceback)
    print("Error: 无法发送邮件")


