from requests import request
import status_list 

txt2=status_list.stat_check()
class m_essage:
 def msgapi(self,ms3,ph3):
 
     url = "https://api.txtbox.in/v1/sms/send"
     payload = "mobile_number=${ms3}&sms_text=helloWorld&sender_id=market"
     headers = {
       'apiKey': "9f81fddf27be1aa3e73a0619392cbc0c",
       'content-type': "application/x-www-form-urlencoded",
       }
     response = request("POST", url, data=payload, headers=headers)
     print(response.text)
    
     txt2.text_fl2(ph3)
    