from blog.celery import app
from helper import fake_content
from news.models import News


@app.task
def create_news():
    title = fake_content.get_title()
    content = fake_content.get_content()
    news = News.objects.create(title=title, content=content)
    news.save()
