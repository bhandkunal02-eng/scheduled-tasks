import smtplib
import datetime as dt
import random
user_mail="bhand.kunal03@gmail.com"
password="skbr mpgc ixen uosy"
now=dt.datetime.now()
weekday=now.weekday()  
if weekday== 5:
    with open("E:\Pyhon Basic to Advance ,Udemy\Python-Day-32_email\Birthday+Wisher+(Day+32)+start\Birthday Wisher (Day 32) start\quotes.txt","r") as quote_file:
        
        all_quotes=quote_file.readlines()
        quote=random.choice(all_quotes)


    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=user_mail,password=password)
        connection.sendmail(from_addr=user_mail,to_addrs="bhand.kunal04@gmail.com",msg=f"Subject:Monday Quote\n\n {quote}")



