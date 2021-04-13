import smtplib
usermail='tomahawx3@gmail.com'
msg='HI again'
def bill(usermail,msg):
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login('tomahawx3@gmail.com', 'db210401')
        smtp.sendmail('tomahawx3@gmail.com', usermail, msg)
bill(usermail, msg)