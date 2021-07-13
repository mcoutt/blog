from rest_framework import viewsets
from news.models import News
from news.serializers import NewsSerializer


class NewsViewset(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
