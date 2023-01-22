import re
from mytimezone import dt11, dt22
import email_api

e_send = email_api.e_mail()

class email_valid:
 def email_val(self,ms2,em2,ph2,con2,sch2):
  with open('em_stat.txt', 'r') as fq:
   lines = fq.read()
      
   if em2 not in lines:
     regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
     if(re.fullmatch(regex, em2)):
         
             if (len(sch2)==0 or sch2==dt11) and con2 == "USA" :
               e_send.emailsender(ms2,em2,ph2)
             elif (len(sch2)==0 or sch2==dt22) and con2 == "INDIA":
               e_send.emailsender(ms2,em2,ph2)
             else:
              
               print("scheduled later")
     else:
          
          print("email address is INVALID")
   else:
    
    print("Email already sent") 