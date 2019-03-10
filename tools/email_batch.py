# _*_ coding:utf-8 _*_
__author__ = 'Sheldon'
__date__ = '2019/3/9 15:06'
from datetime import datetime
from multiprocessing import Pool,Process
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import mimetypes
import os


from exchangelib import Credentials, Account, Message, Mailbox, FileAttachment


class Job(object):

    def __init__(self, frequence, due_time, loop=None):
        """
        :param frequence: 执行频率 m-分钟 h-小时 d-天 M-月 y-年
        :param due_time: 截止时间，到了截止时间即停止运行
        :param loop: 任务执行次数
        """
        self._frequence = frequence if frequence is not None else 'm'
        self._due_time = due_time if due_time is not None else -1
        self._loop = loop if loop is not None else -1

    @property
    def frequence(self):
        return self._frequence

    @frequence.setter
    def frequence(self, value):
        if value not in ('m', 'h', 'd', 'M', 'y'):
            raise ValueError('赋值需要在规定区间：执行频率 m-分钟 h-小时 d-天 M-月 y-年')
        self._frequence = value

    def run(self):
        if self._due_time == -1:
            pass


class MailServer(object):

    def __init__(self, user, password, server_type, host, port=None):
        self._user = user
        self._password = password
        self._port = port
        self._server_type = server_type
        self._host = host
        self._server = None
        self._email = None
        self._from = None
        self._to = []
        self._bcc = []
        self._cc = []

    def _build_email_smtp(self, message_text=None, subject=None):
        # MIMEMultipart中的收件人只是邮件内容显示，需传入str 而不是list
        message = MIMEMultipart()
        self._from = message['From'] = self._user
        message['Subject'] = subject if subject is not None else ""
        if len(self._to) > 0:
            message['To'] = ';'.join(self._to)
        if len(self._cc) > 0:
            message['Cc'] = ';'.join(self._cc)
        if len(self._bcc) > 0:
            message['Bcc'] = ';'.join(self._bcc)
        msg_text = MIMEText(message_text, 'plain', 'utf-8')
        message.attach(msg_text)
        return message

    def _build_email_exchange(self, message_text=None, subject=None):
        message = Message(
            account=self._server,
            subject=subject,
            body=message_text,
            to_recipients=[Mailbox(email_address=addr) for addr in self._to if addr is not None],
            cc_recipients=[Mailbox(email_address=addr) for addr in self._cc if addr is not None],
            bcc_recipients=[Mailbox(email_address=addr) for addr in self._bcc if addr is not None],

        )
        return message

    def send_email(self, receivers, message_text=None, subject=None, attachments=None,  cc=None, bcc=None):
        """

        :param receivers: list 收信人
        :param message_text:  str 邮件内容
        :param subject: str 邮件标题
        :param attachments:  list [fileurl] 存放附件的路径列表
        :param cc: list[str] 抄送地址
        :param bcc: list[str] 密送地址
        :return: None
        """
        self._connect()
        get_eaddr = lambda email_lists: email_lists if isinstance(email_lists, list) else [email_lists]
        if receivers:
            self._to = get_eaddr(receivers)
        if cc:
            self._cc = get_eaddr(cc)
        if bcc:
            self._bcc = get_eaddr(bcc)
        if self._server_type == 'smtp':
            msg = self._build_email_smtp(message_text=message_text, subject=subject)
        elif self._server_type == 'exchange':
            msg = self._build_email_exchange(message_text=message_text, subject=subject)
        if attachments is not None:
            self._add_attachments(msg, attachments)
        self._send_email(msg)

    def _add_attachments(self, message, attachments):
        for attachment in attachments:
            with open(attachment, 'rb') as f:
                path, filename = os.path.split(attachment)
                if self._server_type == 'smtp':
                    attach = MIMEApplication(f.read())
                    attach['Content-type'] = mimetypes.guess_type(attachment)[0]
                    attach.add_header('Content-Disposition', 'attachment', filename=filename)
                elif self._server_type == 'exchange':
                    attach = FileAttachment(name=filename, content=f.read())
                message.attach(attach)

    def _connect_smtp(self):
        import smtplib
        try:
            if self._port is None:
                self._port = 25
            self._server = smtplib.SMTP(host=self._host, port=self._port)
            self._server.login(user=self._user, password=self._password)
            return True
        except Exception as e:
            raise e

    def _connect_exchange(self):
        try:
            credits = Credentials(username=self._user, password=self._password)
            self._server = Account(primary_smtp_address=self._host, credentials=credits, autodiscover=True)
        except Exception as e:
            print(e)
            raise e

    def _connect(self):
        status = False
        if self._server_type == 'smtp':
            status = self._connect_smtp()
        elif self._server_type == 'exchange':
            status = self._connect_exchange()
        return status

    def _send_email(self, message):
        try:
            if self._server_type == 'smtp':
                tolist = self._to + self._cc + self._bcc
                self._server.sendmail(from_addr=self._from, to_addrs=tolist,msg=message.as_string())
            elif self._server_type == 'exchange':
                message.send()
            else:
                print("other error happened")
            print(f"email sent successfully at {datetime.now()}")
        except Exception as e:
            print(e)
            raise e
        finally:
            if self._server_type == 'smtp':
                self._server.quit()
            print(f"exit")


if __name__ == '__main__':
    mail = MailServer(user='test', password='XXXX',
                      server_type='exchange',
                      host='stest'
                      )
    mail.send_email(receivers='xi47@163.com', message_text='你好，我是中国小伙子',
                     subject='测试邮件', bcc='sss',
                     attachments=['E:/公司作业/(2019-01-15)核心报表/中文附件.xlsx',
                                  'E:/公司作业/(2019-01-15)核心报表/mail_utils.py']
                    )

