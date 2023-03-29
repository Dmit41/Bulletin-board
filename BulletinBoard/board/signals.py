from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

from django.core.mail import EmailMultiAlternatives
from .models import Response


@receiver(post_save, sender=Response)
def add_response(sender, instance, created, **kwargs):
    if created:
        subject = f'{instance.author} откликнулся на ваше объявление!'
        text = f'{instance.text} \nПосмотреть все отклики можно на: http://127.0.0.1:8000/response/ '
        mail = [instance.post.author.email]
    else:
        if instance.status:
            subject = f'{instance.post.author} принял ваш отклик!'
            text = f'Это отличный повод посетить наш сайт: http://127.0.0.1:8000'
        else:
            subject = f'{instance.post.author} передумал... наверное(('
            text = f'Но не расстраивайтесь!\nЗато вы можете посетить наш сайт: http://127.0.0.1:8000 '
        mail = [instance.author.email]

    msg = EmailMultiAlternatives(
        subject=subject,
        body=text,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=mail
    )

    msg.send()
