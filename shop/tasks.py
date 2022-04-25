import time

from celery import shared_task
from django.core.mail import send_mail

# @shared_task
from shop.celery import app


@app.task
def send_confirmation_email(code, email):
    time.sleep(10)
    full_link = f'http://localhost:8000/account/activate/{code}'
    send_mail(
        'Привет', # title
        full_link, # body
        'vladislav001015@gmail.com', # from email
        [email] # to email
    )
