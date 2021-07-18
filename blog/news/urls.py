from rest_framework import routers
from django.urls import path
from news.views import NewsModelViewset, main_page

app_name = 'news'

router = routers.DefaultRouter()
router.register('news', NewsModelViewset, basename='news')
router.register('<slug:slug>', NewsModelViewset, basename='get_one_news')

urlpatterns = [
        path('', main_page)
    ] + router.urls
