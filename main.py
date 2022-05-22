import smtplib

my_email = "Aleshichevigor@outlook.com"
password = "45rhfy7853rt"
connection = smtplib.SMTP("outlook.office365.com")
connection.starttls()     # защита письма
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs="Aleshichevigor@yahoo.com",
                    msg="Subject:Hello Igor\n\nThi is my first message to you.")
connection.close()

import datetime as dt     #переименовали

now = dt.datetime.now()
year = now.year
if year == 2022:
    print("Yahoo")
month = now.month
day_of_week = now.weekday()
data_of_birthday = dt.datetime(year= 1995, month= 12, day= 15, hour=4)
print(data_of_birthday)