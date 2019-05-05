import smtplib

host = 'smtp.gmail.com'
port = 587
username = input('Enter user email: ')
password = input('Enter user password: ')
from_email = username
to_list = ['polymathfreeman@gmail.com', 'becomefreerichman@gmail.com']

email_conn = smtplib.SMTP(host, port)
email_conn.ehlo()
email_conn.starttls()
email_conn.login(username, password)
email_conn.sendmail(from_email, to_list, 'Hello there is an email message from Python')
email_conn.quit()

from smtplib import SMTP

ABC = smtplib.SMTP(host, port)
ABC.ehlo()
ABC.starttls()
ABC.login(username, password)
ABC.sendmail(from_email, to_list, 'Hello there is an email message from Python')
ABC.quit()

from smtplib import SMTP, SMTPAuthentificationError, SMTPException

pass_wrong = smtplib.SMTP(host, port)
pass_wrong.ehlo()
pass_wrong.starttls()
try:
    pass_wrong.login(username, 'wrong_password')
    pass_wrong.sendmail(from_email, to_list, 'Hello there is an email message from Python')
except SMTPAuthentificationError:
    print('Could not login')
except:
    print('An error occurred')

pass_wrong.quit()

