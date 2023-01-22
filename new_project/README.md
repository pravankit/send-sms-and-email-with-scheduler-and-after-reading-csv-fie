#This is a readme file of this Assignment

##Breif about all the files used in this project.

[-]*** Run the program through main.py ****

[-]**app.py**- To get the logs details of the project. It will a file named "log.text", having the logs details and errors.

[-]**email_api.py** - it will call email sending api, after getting the inputs from "email_validation.py", which will validate the email address, based on given parameters.

[-]**em_stat.txt** - write in itself the email address, to which the email has been sent.(used to avoid duplictaion)

[-]**ms_stat.txt** - write in itself the phone numbers, to which the text message has been sent.(used to avoid duplictaion).

[-]**msg_apisms.py**- used to send text messages, after getting the inputs from "msg_validation.py", which is used to check the differnt parameters like phone no digits, time constraints, country utc etc.

[-]**mytimezone.py**- this is used to get the exact time in INDIA and USA, used to get the date to compare the schedule on date of input csv file.

[-]**requirements.txt**- contains the list of requirements of modules and libraries used in this project.

[-]**status_list.py**- contains the methods to create em_stat.txt and ms_stat.txt.
...........................................................................................
In worker.py rocketry is used to schedule the program to run after each 8 seconds to check for the scheduled on rows.

[-]**worker.py**- this contains the methods which will read the csv file rows which are scheduled on differnt dates and call the apis(run the program for those rows) after every 8seconds. This will get executed after mains.py.

[-]**mains.py** - this will run the program after reading the csv file for the very first time and give command to validation method to validate the input, which will further call the apis.