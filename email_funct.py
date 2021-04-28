import smtplib

def notify_user(email, pw, user_from, user_to, body_text):

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo_or_helo_if_needed()
        server.login(user=email, password=pw)
        server.sendmail(from_addr=user_from, to_addrs=user_to, msg=body_text)
        server.close()

        print('email sent!')
    except:
        print('notify_user failed!')