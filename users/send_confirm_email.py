from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .token_generator import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from hms.settings import DOMAIN

def send_confirmation_email(user):
    email_subject = 'Activate Your Account'
    message = render_to_string('activate_account.html', {
        'user': user,
        'domain': DOMAIN,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
    })
    to_email = user.email
    email = EmailMessage(email_subject, message, to=[to_email])
    email.send()
    return HttpResponse('We have sent you an email, please confirm your email address to complete registration')
