import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import News
from ..serializers import NewsSerializer

# initialize the APIClient app
client = Client()


class GetAllNewsTest(TestCase):
    """ Test module for GET all news API """

    def setUp(self):
        News.objects.create(
            title='Test Title', content='Test Content')
        News.objects.create(
            title='Test Another Title', content='Test Another Content')

    def test_get_all_news(self):
        # get API response
        response = client.get(reverse('news_api-list'))
        # get data from db
        news = News.objects.all()
        serializer = NewsSerializer(news, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetSingleNewsTest(TestCase):
    """ Test module for GET single news API """

    def setUp(self):
        self.test_title = News.objects.create(
            title='Test Title', content='Test Content')
        self.test_another_title = News.objects.create(
            title='Test Another Title', content='Test Another Content')

    def test_get_valid_single_news(self):
        response = client.get(
            reverse('news_api-detail', kwargs={'pk': self.test_title.pk}))
        news = News.objects.get(pk=self.test_title.pk)
        serializer = NewsSerializer(news)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_news(self):
        response = client.get(
            reverse('news_api-detail', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateNewNewsTest(TestCase):
    """ Test module for inserting a new news """

    def setUp(self):
        self.valid_payload = {
            'title': 'Test Another Title',
            'content': 'Test Another Content',
        }
        self.invalid_payload = {
            'Wrong-title': 'Test Wrong Title',
            'Wrong-content': 'Test Wrong Content',
        }

    def test_create_valid_news(self):
        response = client.post(
            reverse('news_api-list'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_news(self):
        response = client.post(
            reverse('news_api-list'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UpdateSingleNewsTest(TestCase):
    """ Test module for updating an existing news record """

    def setUp(self):
        self.test_title = News.objects.create(
            title='Test Title', content='Test Content')
        self.test_another_title = News.objects.create(
            title='Test Another Title', content='Test Another Content')
        self.valid_payload = {
            'title': 'Test Valid Title',
            'content': 'Test Valid Content',
        }
        self.invalid_payload = {
            'Wrong-title': 'Test Wrong Title',
            'Wrong-content': 'Test Wrong Content',
        }

    def test_valid_update_news(self):
        response = client.put(
            reverse('news_api-detail', kwargs={'pk': self.test_another_title.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_update_news(self):
        response = client.put(
            reverse('news_api-detail', kwargs={'pk': self.test_another_title.pk}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteSingleNewsTest(TestCase):
    """ Test module for deleting an existing news record """

    def setUp(self):
        self.test_title = News.objects.create(
            title='Test Title', content='Test Content')
        self.test_another_title = News.objects.create(
            title='Test Another Title', content='Test Another Content')

    def test_valid_delete_news(self):
        response = client.delete(
            reverse('news_api-detail', kwargs={'pk': self.test_another_title.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_news(self):
        response = client.delete(
            reverse('news_api-detail', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
