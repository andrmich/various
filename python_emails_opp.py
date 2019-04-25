"""Opportunistic Encryption With starttls()"""

import smtplib, ssl

smtp_server= 'smtp.gmail.com'
port = 587

sender = input('Enter your email here, please: ')
password = input('Enter your password here, please: ')

context = ssl.create_default_context()

try:
    server = smtplib.SMTP(smtp_server, port)
    server.ehlo()
    server.starttls(context=context)
    server.ehlo()
    server.login(sender, password)
    # send mail
    print('It worked.')
except Exception as e:
    print(e)
finally:
    server.quit()


