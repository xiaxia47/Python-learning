# -*- coding:gbk
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.utils import parseaddr,formataddr
import smtplib

def _format_addr(s):
    name,addr = parseaddr(s)
    return formataddr((Header(name,'utf-8').encode(),addr))

from_addr = 'XXX'
password = 'XXXX'
to_addr = 'XXX'
smtp_server = 'XXX'

#msg = MIMEText('hello, send by Python...','plain','utf-8')
msg = MIMEMultipart()
msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候....','utf-8').encode()

msg.attach(MIMEText('send with file....','plain','utf-8'))

with open('C:/Users/Public/Pictures/Sample Pictures/desert.jpg' ,'rb') as f:
    mime = MIMEBase('image','jpg',filename='desert.jpg')
    mime.add_header('Content-Disposition','attachment',filename='desert.jpg')
    mime.add_header('Content-ID','<0>')
    mime.add_header('X-Attachment-Id','0')
    mime.set_payload(f.read())
    encoders.encode_base64(mime)
    msg.attach(mime)
    
print('smtplib')
server = smtplib.SMTP(smtp_server,25)
server.starttls()
print('debuglevel')
server.set_debuglevel(1)
print('login')
server.login(from_addr,password)
print('sendmail')
server.sendmail(from_addr,[to_addr],msg.as_string())
print('quit')
server.quit()
