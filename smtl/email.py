import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config import email_config
from smtl.logging import logger


class EMail:
    def __init__(self, host, port=None, addr='', user=None, password=None):
        self.host = host
        self.port = port or 587
        self.addr = addr
        self.user = user or addr
        self.password = password

    def create_connection(self, ):
        connection = smtplib.SMTP(self.host, self.port)
        connection.login(self.user, self.password)
        return connection

    def send(self, from_addr=None, to_addr=None, subject='', body=''):
        msg = MIMEMultipart()
        msg['From'] = from_addr or self.addr
        msg['To'] = to_addr or self.addr
        msg['Subject'] = subject
        msg.attach(MIMEText(body))

        try:
            conn = self.create_connection()
            conn.sendmail(msg['From'], msg['To'], msg.as_string())
            conn.quit()
        except smtplib.SMTPException as e:
            logger.error('Error sending mail: ' + str(e))


if email_config:
    default_mail = EMail(
        host=email_config['HOST'],
        port=email_config.get('PORT'),
        addr=email_config.get('ADDR'),
        user=email_config.get('USER'),
        password=email_config['PASSWORD']
    )
else:
    default_mail = None
