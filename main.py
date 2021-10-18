import datetime as dt
import pandas
import random
import smtplib

df = pandas.read_csv('birthdays.csv')
birthdays = df.to_dict(orient="records")

today = dt.datetime.now()
today_month = today.month
today_day = today.day

my_email = "blairequeensmtp@yahoo.com"
password = "eyckhyzvvmggmozc"

for friend in birthdays:
    if friend['month'] == today_month and friend['day'] == today_day:
        num = random.randint(1, 3)
        letter = f'letter_templates/letter_{num}.txt'
        with open(letter) as data:
            text = data.read()
            personalized_letter = text.replace('[NAME]', friend['name'])

        with smtplib.SMTP('smtp.mail.yahoo.com') as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=friend['email'],
                msg=f"Subject: Happy Birthday!\n\n{personalized_letter}"
            )
