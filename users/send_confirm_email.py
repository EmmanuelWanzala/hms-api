from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .token_generator import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from hms.settings import DOMAIN,SENDGRID_API_KEY
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail








def send_confirmation_email(user):

    # locates our email.html in the templates folder
    msg_html = render_to_string('activate_account.html',{
        'user': user,
        'domain': DOMAIN,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
    })
    message = Mail(
        # the email that sends the confirmation email
        from_email='dennismuriithik@gmail.com',
        to_emails=[user.email],  # list of email receivers
        subject='Account activation',  # subject of your email
        html_content=msg_html)
    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
        print(response.status_code)
    except Exception as e:
        print(e.message)
        return str(e)





