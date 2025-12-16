import smtplib # simple email transfer protocal
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# seder details
SENDER_EMAIL = "chfarooq2001@gmail.com"
SENDER_PASSKEY= "vhff iyft gfte opdj"
# smtp configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

# single email send function defination
def singleEmailSender(to_email:str, subject:str, body:str):
    msg = MIMEMultipart()
    msg['To'] = to_email
    msg['From'] = SENDER_EMAIL
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # create server connection
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        # server starts sequerly
        server.starttls()
        # login to server
        server.login(SENDER_EMAIL, SENDER_PASSKEY)
        # send email to to_email
        server.sendmail(SENDER_EMAIL, to_email, msg=msg.as_string())
        #server quit
        server.quit()
    except Exception as e:
        print(f"Field to send email to {to_email}:,{e}")


