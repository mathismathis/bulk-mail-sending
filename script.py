import pandas as pd
import smtplib

excel= pd.read_excel("gmail.xlsx")
gmails = excel['gmails'].values
print(gmails)

username=""
password=""

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(username,password)
print("login suscess")

msg = "hi Welcome"
subject = "Testing"
body = "Subject: {}\n\n{}".format(subject,msg)

for mail in gmails:
    server.sendmail(username, mail, body)
server.quit()
