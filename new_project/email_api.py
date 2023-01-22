import csv, smtplib, re
from email.message import EmailMessage
import status_list 

txt1 = status_list.stat_check()
class e_mail:
 def emailsender(self,ms1,em1,ph1):
     server = smtplib.SMTP('smtp.gmail.com',587)
     server.starttls()
     server.login('abcitdemo110@gmail.com','fsllwkkdqkghvsyw')
     subject = "Mail from ankit.pvt.ltd"
     sender = "abcitdemo110@gmail.com"
     email= EmailMessage()
     email['From']= sender
     email['To'] = em1
     email['subject'] = subject
     email.set_content(ms1)
     server.send_message(email)
     
    
     print(f'Sent to {ph1}')
     txt1.text_fl1(em1)

