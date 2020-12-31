from config import S3_ACCESS_KEY, S3_SECRET_ACCESS_KEY, S3_BUCKET,S3_LOCATION,PORT,SMTP_SERVER,SENDER_EMAIL,PASSWORD
import boto3
import smtplib, ssl
import time

s3 = boto3.client("s3",
aws_access_key_id=S3_ACCESS_KEY,
aws_secret_access_key=S3_SECRET_ACCESS_KEY)



def execute_task(receiver_email,message):

    print("Starting task, gonna sleep for 5 seconds")
    time.sleep(5)
        
    send_email(receiver_email,message)
    
    print("Ending task")


def send_email(receiver_email,message):
    msg = """\
Subject: Hi there,

This message is sent from Python. """ + message

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(SMTP_SERVER, PORT, context=context) as server:
        server.login(SENDER_EMAIL, PASSWORD)
        server.sendmail(SENDER_EMAIL, receiver_email, msg)


