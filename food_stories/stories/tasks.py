import time
from datetime import datetime, timedelta

from django.conf import settings
from django.core.mail import EmailMessage

from celery import shared_task

from django.template.loader import render_to_string

from stories.models import Subscriber, Recipe, Story


@shared_task
def send_mail_to_subscribers():
    subscribers = Subscriber.objects.distinct('email').values_list('email', flat=True)

    yesterday = datetime.today() - timedelta(days=1)
    recipes = Recipe.objects.filter(created_at__gte=yesterday)
    stories = Story.objects.filter(created_at__gte=yesterday)

    body = render_to_string('email-subscribers.html', context={
        'recipes': recipes,
        'stories': stories,
        'SITE_ADDRESS': settings.SITE_ADDRESS
    })
    msg = EmailMessage(subject='Stories News', body=body,
                       from_email=settings.EMAIL_HOST_USER, to=subscribers, )
    msg.content_subtype = 'html'
    msg.send()

# def add(a, b, c):
#     ab = a + b
#
#     return multiple(ab, c)
#
# def multiple(ab, c):
#     return ab * c

# @shared_task
# def dump():
#     print('ise dusdu')
#     time.sleep(20)
#     print('dayandi')
