import smtplib
import random
import datetime as dt

my_mail = "adnantesting85@gmail.com"
password = "asdfg@123"


now = dt.datetime.now()
weekday = now.weekday()
if weekday == 2:
    with open("quotes.txt") as quotes_file:
        all_quotes = quotes_file.readlines()
        quote = random.choice(all_quotes)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_mail, password)
        connection.sendmail(from_addr=my_mail, to_addrs=my_mail,
                            msg=f"Subject:Today's Quote\n\n{quote}")