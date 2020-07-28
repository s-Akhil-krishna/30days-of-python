
#package to send mails with smtp servers
import smtplib

#for 
from email.mime.text import MIMEText

#for handling text,html
from email.mime.multipart import MIMEMultipart

username    = 'ptt.trail.email@gmail.com' 
password    = 'Cognitive@2'
from_email  = 'Akhil <ptt.trail.email@gmail.com>'


def send_mail(  from_email=from_email,
                to_emails=None,
                subject='Welcome',
                text='Hey There!',
                html = None):

    assert isinstance(to_emails,list)
    #Throws an error if we dint pass-in a emails as a list.
    msg = MIMEMultipart('alternative')
    msg['From']     = from_email
    msg['To']       = ", ".join(to_emails)
    msg['Subject']  = subject

    txt_part        = MIMEText(text,'plain')
    msg.attach(txt_part)
    
    if html!=None:
        html_part       = MIMEText(html,'html')
        msg.attach(html_part)

    
    msg_str         = msg.as_string()

    #creating a server session

    server          = smtplib.SMTP(host='smtp.gmail.com',port=587)
    server.ehlo()#testing 
    server.starttls()#security 
    server.login(username,password)
    server.sendmail(from_email,to_emails,msg_str)
    server.quit()#ending the session
    sent = True

    sent = False
   
