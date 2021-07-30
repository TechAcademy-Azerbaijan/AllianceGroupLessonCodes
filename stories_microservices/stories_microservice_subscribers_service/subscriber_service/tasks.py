from .config.celery import celery
from flask import render_template
from .cache import Cache
from .models import Subscriber
from .publisher import Publish


@celery.task(name='send_mail_to_subscribers', task_time_limit=60, task_soft_time_limit=50,
             acks_late=True, autoretry_for=(Exception,), retry_backoff=True,
             retry_jitter=False, retry_kwargs={'max_retries': 3}, retry_backoff_max=60)
def send_mail_to_subscribers():
    posts = Cache().read()
    if not posts:
        return
    # print('posts', type(list(posts)))
    html = render_template('subscribers_email.html', recipes=posts)
    subject = "Stoies daily digest"
    user_emails = Subscriber.query.with_entities(Subscriber.email)
    emails = []
    for email in user_emails:
        emails.append(email[0])
    print(emails)
    Publish(event_type='send_mail', data={
        'body': html,
        'subject': subject,
        'recipients': emails
    })

# celery -A subscriber_service.config.celery worker --loglevel=INFO -B