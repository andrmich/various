"""Send emails with Python using smtplib, secure from the start."""

import smtplib, ssl
import getpass

smtp_server = 'smtp.gmail.com'
port = 465

sender = input('Enter your email here, please: ')
password = getpass.getpass('Enter your password here, please: ')

receiver = input('Enter your receiver email here, please: ')
message = '''
From {}
To {} 
Subject: Hi There!

This message was sent from Python! How are you?
'''.format(sender, receiver)

context = ssl.create_default_context()

with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender, password)
    print('It worked!')
    # send mail
    server.sendmail(sender, receiver, message)
