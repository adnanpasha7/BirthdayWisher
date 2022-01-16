import random

import pandas
import smtplib
import datetime as dt

my_email = "adnantesting85@gmail.com"
password = "asdfg@123"

# 2. Check if today matches a birthday in the birthdays.csv
today = dt.datetime.now()
today_tuple = (today.month, today.day)
data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    birthdays_person = birthdays_dict[today_tuple]
    filepath = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(filepath) as letter:
        contents = letter.read()
        contents = contents.replace("[NAME]", birthdays_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(from_addr=my_email, to_addrs=birthdays_person["email"],
                            msg=f"Subject:Happy Birthday!\n\n{contents}")




