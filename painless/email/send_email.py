from django.conf import settings
from django.core.mail import send_mail


def email_service(to, subject, message):
    send_mail(
        subject,
        message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=to
    )
