import smtplib

my_email = "Aleshichevigor@outlook.com"
password = "45rhfy7853rt"
connection = smtplib.SMTP("outlook.office365.com")
connection.starttls()     # защита письма
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs="Aleshichevigor@yahoo.com",
                    msg="Subject:Hello Igor\n\nThi is my first message to you.")
connection.close()
