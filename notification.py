import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText




def sendNotification(self,personName):
        sender = 'codingbug.py@gmail.com'
        receiver = 'photogenicbug@gmail.com'
        password = '*********'

        message = f"Unknown Person Detected at {datetime.datetime.now()}"
        server = smtplib.SMTP_SSL(host='smtp.gmail.com',port=465)
        server.login(sender,password)

        msg = MIMEMultipart()
        msg['From'] = sender
        msg['To'] = receiver
        msg['Subject'] = 'Message from Door Unlocking System'
        msg.attach(MIMEImage(open(r'detected.jpg','rb').read(),name='detectedface'))
        msg.attach(MIMEText(message,'plain'))

        server.send_message(msg)
        print('Email sent')
        server.quit()