import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate

FROM_ADDRESS = 'sender mail address'
MY_PASSWORD = 'sender mail password'
TO_ADDRESS = 'recipient mail address'
BCC = ''
SUBJECT = 'Indicator_matched'

class Send_alert:

    def create_message(self,from_addr, to_addr, bcc_addrs, subject, malURL, URL, src):
        malURL = malURL.replace('.','[.]')
        URL = URL.replace('.','[.]')
        body = 'Proxy log matched with indicator: ' + malURL + '\n' + URL + '\n' + 'Source IP:' + src
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = from_addr
        msg['To'] = to_addr
        msg['Bcc'] = bcc_addrs
        msg['Date'] = formatdate()
        return msg


    def send(self,from_addr, to_addrs, msg):
        smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
        smtpobj.ehlo()
        smtpobj.starttls()
        smtpobj.ehlo()
        smtpobj.login(FROM_ADDRESS, MY_PASSWORD)
        smtpobj.sendmail(from_addr, to_addrs, msg.as_string())
        smtpobj.close()

    def __init__(self, malURL, URL, src):
        to_addr = TO_ADDRESS
        subject = SUBJECT
        msg = self.create_message(FROM_ADDRESS, to_addr, BCC, subject, malURL, URL, src)
        self.send(FROM_ADDRESS, to_addr, msg)