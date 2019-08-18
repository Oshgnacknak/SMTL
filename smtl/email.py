import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config import email_config
from smtl.logging import logger


class EMail:
    def __init__(self, host, port=None, addr=''):
        self.server = smtplib.SMTP(host, port or 587)
        self.addr = addr

    def login(self, user=None, password=''):
        self.server.login(user or self.addr, password)

    def is_connected(self):
        try:
            status = self.server.noop()[0]
        except smtplib.SMTPServerDisconnected:
            status = -1
        return True if status == 250 else False

    def send(self, from_addr=None, to_addr=None, subject='', body=''):
        msg = MIMEMultipart()
        msg['From'] = from_addr or self.addr
        msg['To'] = to_addr or self.addr
        msg['Subject'] = subject
        msg.attach(MIMEText(body))

        if not self.is_connected():
            self.server.connect()
        self.server.sendmail(msg['From'], msg['To'], msg.as_string())


if email_config:
    default_mail = EMail(
        host=email_config['HOST'],
        port=email_config.get('PORT'),
        addr=email_config.get('ADDR')
    )
    default_mail.login(
        user=email_config.get('USER'),
        password=email_config['PASSWORD']
    )
    logger.info('EMail logged in: ' + default_mail.addr)
else:
    default_mail = None
