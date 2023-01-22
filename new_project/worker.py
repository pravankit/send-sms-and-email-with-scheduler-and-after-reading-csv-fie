import csv
import email_validation
import msg_validation 
from rocketry import Rocketry
import time as tm
from datetime import datetime

e_vad1= email_validation.email_valid()
m_vad1=msg_validation.msg_valid()

my_work = Rocketry() 
@my_work.task('every 8 sec')   
def jobb():
 
  with open('Sample.csv','r') as file:
   reader = csv.reader(file)
   next(reader)
   
   for ms,em,ph,con,sch in reader:
     if len(sch)!=0:
         e_vad1.email_val(ms,em,ph,con,sch)
         m_vad1.textmsg(ms,em,ph,con,sch)
   
 
if __name__=="__main__":
    my_work.run()