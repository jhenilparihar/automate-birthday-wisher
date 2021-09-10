import smtplib
import random
import datetime as dt
import pandas

now = dt.datetime.now()
day = now.day
month = now.month
today = (month, day)
data = pandas.read_csv("birthdays.csv")

birthdays_dict = {(data_row['month'], data_row['day']): data_row for (index, data_row) in data.iterrows()}

if today in birthdays_dict:
    print(birthdays_dict[today]['name'])
    letter_format = random.choice(['letter_1.txt', 'letter_2.txt', 'letter_3.txt'])
    with open(f'letter_templates/{letter_format}') as file:
        letter = file.read()
    letter = letter.replace('[NAME]', birthdays_dict[today]['name'])
    print(letter)

    my_email = 'YOUR EMAIL ADDRESS'
    password = 'YOUR EMAIL PASSWORD'

    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=birthdays_dict[today]['email'],
                            msg=f"Subject: Happy Birthday\n\n{letter}")
    print('Done')
