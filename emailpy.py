import smtplib, ssl
import textfile as tf
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def sendMail (plaintext, htmltext):
    sender = 'notifier@onedigitalmedia.com'
    mail_user = sender
    mail_to = tf.getSetting('mail_to')
    mail_password = 'Vodo9440'

    msg = MIMEMultipart('alternative')
    msg['Subject'] = 'ADM OFFLINE DEVICES'
    msg['From'] = sender
    msg['To'] = mail_to
    plaintext = plaintext
    htmltext = htmltext

    #turn plaintext and html text into MIMEText objects
    part1 = MIMEText(plaintext, 'plain')
    part2 = MIMEText(htmltext, 'html')

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    msg.attach(part1)
    msg.attach(part2)

    try:
        context = ssl.create_default_context()
        with smtplib.SMTP('smtp.office365.com', 587) as server:
            server.ehlo()
            server.starttls()
            server.login(mail_user, mail_password)
            server.sendmail(sender, mail_to, msg.as_string())
        print ("Email sent successfully!")
    except Exception as ex:
        print ("Something went wrong….",ex)


# def sendMail(text):
#     mail_user = 'notifier@onedigitalmedia.com'
#     mail_password = 'Vodo9440'
#     sent_from = mail_user
#     to = tf.getSetting('mail_to')
#
#     subject = 'ADM OFFLINE DEVICES'
#     body = text
#
#     email_text = """\
#     From: %s
#     To: %s
#     Subject: %s
#
#     %s
#     """ % (sent_from, ", ".join(to), subject, body)
#
#     try:
#         smtp_server = smtplib.SMTP('smtp.office365.com', 587)
#         smtp_server.ehlo()
#         smtp_server.starttls()
#         smtp_server.login(mail_user, mail_password)
#         smtp_server.sendmail(sent_from, to, email_text)
#         smtp_server.close()
#         print("Email sent successfully!")
#     except Exception as ex:
#         print("Something went wrong….", ex)