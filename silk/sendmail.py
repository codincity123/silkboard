from operator import imod
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.utils.html import strip_tags

def sendMailUser(toemail,usename):
    template = render_to_string('email_template.html',{'name':usename})
    email = EmailMessage(
            "Record Added",
            strip_tags(template),
            settings.EMAIL_HOST_USER,
            to= [toemail],
        )
    email.send()