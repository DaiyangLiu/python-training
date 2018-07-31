import time
import sys
import os
from check_electric import check_electric1
import smtplib
from email.mime.text import MIMEText
from email.header import Header


while( os.system('ping www.baidu.com')==1):   #当状态为未联网状态时
    print('沉睡60秒')
    time.sleep(30)

#获取电量
value=check_electric1()
print(value)


if value < 30 :
    # 发件人和收件人
    sender = 'ldy_robot@126.com'
    receiver = 'daiyang_liu@163.com'

    # 所使用的用来发送邮件的SMTP服务器
    smtpServer = 'smtp.126.com'

    # 发送邮箱的用户名和授权码（不是登录邮箱的密码）
    username = 'R·Daiyang·Liu'
    password = 'dg1278563'

    mail_title = '该交电费了'
    mail_body = '剩余电量：'+ str(value) +'。大哥您的电费不够了，赶紧交吧'

    # 创建一个实例
    message = MIMEText(mail_body, 'plain', 'utf-8')  # 邮件正文
    message['From'] = sender  # 邮件上显示的发件人
    message['To'] = receiver  # 邮件上显示的收件人
    message['Subject'] = Header(mail_title, 'utf-8')  # 邮件主题

    try:
        smtp = smtplib.SMTP()  # 创建一个连接
        smtp.connect(smtpServer)  # 连接发送邮件的服务器
        smtp.login(username, password)  # 登录服务器
        smtp.sendmail(sender, receiver, message.as_string())  # 填入邮件的相关信息并发送
        print("邮件发送成功！！！")
        smtp.quit()
    except smtplib.SMTPException:
        print("邮件发送失败！！！")







