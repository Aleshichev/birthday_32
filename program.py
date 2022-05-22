import smtplib
import datetime as dt
import random

def send_mail():
    my_email = "Aleshichevigor@outlook.com"
    password = "45rhfy7853rt"
    with smtplib.SMTP("outlook.office365.com") as connection:
        connection.starttls()     # защита письма
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email,
                            msg=f"Subject:Hello Igor\n\n{quote}.")

def day():
    now = dt.datetime.now()
    day_of_week = now.weekday()
    return day_of_week

with open("quotes.txt") as quote_file:
    all_quotes = quote_file.readlines()
    quote = random.choice(all_quotes)


if day() == 6:
    send_mail()