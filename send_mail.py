import smtplib
from email.message import EmailMessage
emails = ['tauhidulhossaintanmoy@gmail.com', 'thtanmoy1@gmail.com']
email = EmailMessage()
email['from'] = 'Tauhidul Hossian'
email['to'] = 'mdnajmulhossain7854@gmail.com', 'tauhidulhossaintanmoy@gmail.com', 'thtanmoy1@gmail.com'
email['subject'] = 'This email is send by python!'

email.set_content('Hello from python programmer.')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login()
    smtp.send_message(email)
    print('all done')
