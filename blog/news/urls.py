from rest_framework import routers
from django.urls import path
from news.views import NewsModelViewSet, main_page

app_name = 'news'

router = routers.DefaultRouter()
router.register('news', NewsModelViewSet, basename='news')
router.register('news/<pk:pk>', NewsModelViewSet, basename='get_one_news')

urlpatterns = [
        path('', main_page)
    ] + router.urls
