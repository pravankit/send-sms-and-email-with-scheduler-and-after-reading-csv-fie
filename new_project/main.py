import csv
import time as tm
from datetime import date
import email_validation
import msg_validation 
import os 


e_vad= email_validation.email_valid()
m_vad=msg_validation.msg_valid()

def main():
 with open('Sample.csv','r') as file:
  reader = csv.reader(file)
  next(reader)
  
  for ms,em,ph,con,sch in reader:
     e_vad.email_val(ms,em,ph,con,sch)
     m_vad.textmsg(ms,em,ph,con,sch)
  

if __name__ == "__main__":
    main()


os.system('python worker.py')