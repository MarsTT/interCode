#coding=utf-8

'''
	假设本机已经支持smtp服务
	使用第三方smtp服务器
'''


import smtplib
from email.mime.text import MIMEText
from email.header import Header

msg = MIMEText("the is the test file")

mail_host = 'smtp.163.com'
mail_user = 'muctianciking@163.com'
#授权码
mail_passwd = 'lovol589673'


sender = 'muctianciking@163.com'
receiver = ['1020006920@qq.com']


# msg['Subject'] = 'An Email Alert'
# msg['From'] = 'muctianciking@163.com'
# msg['To'] = ['1020006920@qq.com']

msg['From'] = Header('this is a test')
msg['To'] = Header('Test!!!')
msg['Subject'] = Header('An Email Alert')


try:
	#s = smtplib.SMTP('127.0.0.1')
	s = smtplib.SMTP()
	s.connect(mail_host,'25')
	s.login(mail_user,mail_passwd)
	s.sendmail(sender,receiver,msg.as_string())
	s.quit()
	print "send success!"
	#s.send_message(msg)
except:
	print "send failure!"