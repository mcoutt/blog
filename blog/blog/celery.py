import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog.settings')

app = Celery('blog')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'add-news-every-5-minutes': {
        'task': 'news.tasks.create_news',
        'schedule': 300.0,
    },
}