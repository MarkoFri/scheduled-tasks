# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.


import pandas as pd
import datetime as dt
import random as rd
import smtplib
import os

dataframe = pd.read_csv('birthdays.csv')
birthday_list = dataframe.to_dict(orient="records")

def check_today(date):
    today = dt.datetime.today()
    return today.month == date.month and today.day == date.day

def create_daily_birthday_list():
    daily_birthday_list = [entry for entry in birthday_list if check_today(dt.date(entry["year"], entry["month"], entry["day"])) ]
    return daily_birthday_list

def send_letters(daily_list):
    for person in daily_list:
        name = person["name"]
        to_address = person["email"]
        with open(f'letter_templates/letter_{rd.randint(1, 3)}.txt', "r") as file:
            data = file.read()
            data = data.replace("[NAME]", name)
        print (data)
        my_email = os.environ.get("MY_EMAIL")
        with smtplib.SMTP('smtp.gmail.com', 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=os.environ.get("MY_PASSWORD")
            connection.sendmail(from_addr=my_email,
                                to_addrs=to_address,
                                msg=f"subject: Happy Birthday, {name}\n\n {data}")

send_letters(create_daily_birthday_list())
