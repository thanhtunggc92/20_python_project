from email.message import EmailMessage
import ssl
import smtplib


email_sender='timmynguyen210792@gmail.com'
password='zhbkbmxhbnnruhmn'

email_receiver='nguyentruongthanhtung@gmail.com'

subject='the subject has been created'
body='the first project in 20 beginer project email sender'

em=EmailMessage()
em['From']=email_sender
em['To']=email_receiver
em['Subject']=subject
em.set_content(body)

context=ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as mail:
    mail.login(email_sender,password)
    mail.sendmail(email_sender,email_receiver,em.as_string())
