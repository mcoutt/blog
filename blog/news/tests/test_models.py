from django.test import TestCase
from ..models import News


class NewsTest(TestCase):
    """ Test module for News model """

    def setUp(self):
        News.objects.create(
            title='Test Title', content='Test Content')
        News.objects.create(
            title='Test Another Title', content='Test Another Content')

    def test_news(self):
        news_title = News.objects.get(title='Test Title')
        news_another_title = News.objects.get(title='Test Another Title')
        self.assertEqual(
            news_title.title, "Test Title")
        self.assertEqual(
            news_another_title.title, "Test Another Title")
