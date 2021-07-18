import os
import fake_content as fake
from news.models import News


def create_news():
    title = fake.get_title()
    content = fake.get_content()
    news = News.objects.create(title=title, content=content)
    news.save()


def run_seed(count=10):
    for _ in range(count):
        create_news()


if __name__ == '__main__':
    run_seed()
