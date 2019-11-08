import smtplib


def send_mail(name, msg):
    server = smtplib.SMTP('smtp.gmail.com', 587)

    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('abhijeetarabhi@gmail.com', 'vlkwpprmfrdmkrfb')

    subject = 'Unknown message from ' + name
    body = 'Message is ' + msg

    message = f'Subject : {subject}\n\n{body}\n'

    server.sendmail('abhijeetarabhi@gmail.com', ['abhijeet_abhi@live.co.uk', 'bandanikhilreddy05@gmail.com'], message)

    print('email sent')


send_mail('Banda', 'Okay')