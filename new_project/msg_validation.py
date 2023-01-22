from mytimezone import dt1,dt11,dt2,dt22
import msg_apisms 


m_send = msg_apisms.m_essage()

class msg_valid:
 def textmsg(self,ms4,em4,ph4,con4,sch4):
  with open('ms_stat.txt', 'r') as fp:
   lines1 = fp.read()
  
   if not ph4 in lines1:
    
     if len(ms4)<=160 and len(ms4)>1 and len(str(ph4))==10 :
         if con4=="USA" and dt1.hour<=17 and dt1.hour>=10 and (len(sch4)==0 or sch4 == dt11):
            m_send.msgapi(ms4,ph4) 

         elif con4=="INDIA" and dt2.hour<=17 and dt2.hour>=10 and (len(sch4)==0 or sch4 == dt22):
            m_send.msgapi(ms4,ph4)
         else:
           
            print("Text message can't be sent as the time has been over OR Scheduled later")  

          
        
     else:
        
         print("INVALID TEXT OR PHONE NUMBER")
   else:
 
    print("Text message already sent")      