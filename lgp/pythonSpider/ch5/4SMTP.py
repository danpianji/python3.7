# -*- coding: UTF-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from email.header import Header
from_addr = "liguangpei1@163.com"
pwd = "密码1z2x3c"#这里需要填写SMTP服务的授权码，163邮箱中的SMTP服务密码

to_addr = "391204514@qq.com"

smtp_server = "smtp.163.com"

msg = MIMEText("爬虫邮箱自动发送测试", "plain", "utf-8")
msg['From']=formataddr(("一号爬虫",from_addr))
msg['To']=formataddr(("管理员",to_addr))
msg['Subject']=Header('一号爬虫运行状态', 'utf-8').encode()

#发送邮件
server = smtplib.SMTP(smtp_server, 25)
server.login(from_addr, pwd)
ret=server.sendmail(from_addr,[to_addr], msg.as_string())
print(ret)
server.quit()
