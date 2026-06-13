import smtplib
import datetime as dt
import random
import os
user_mail=os.environ.get("EMAIL")
password=os.environ.get("PASSWORD")
now=dt.datetime.now()
weekday=now.weekday()  
if weekday== 5:
    with open("quotes.txt","r") as quote_file:
        
        all_quotes=quote_file.readlines()
        quote=random.choice(all_quotes)


    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=user_mail,password=password)
        connection.sendmail(from_addr=user_mail,to_addrs="bhand.kunal04@gmail.com",msg=f"Subject:Good Morning!! Quote\n\n {quote}")



