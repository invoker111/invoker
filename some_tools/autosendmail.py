# coding = utf-8
import smtplib 
from email.mime.text import MIMEText
# 发送方账号密码
send_from="@.com"
password=''

def send_mail(send_to,themetext,maintext):
    # 接收方邮箱地址
    send_to=str(send_to)
    # 邮件主题
    subject=str(themetext)
    # 邮件内容
    content=str(maintext)
    msg=MIMEText(content)
    msg["Subject"]=subject
    msg["From"]=send_from
    msg["To"]=send_to
    # 连接SMTP服务器
    s=smtplib.SMTP_SSL("smtp.qq.com",465)
    # 登陆发送方的邮箱
    s.login(send_from,password)
    # 发送邮件
    s.sendmail(send_from,send_to,msg.as_string())
    print('成功发送！')
