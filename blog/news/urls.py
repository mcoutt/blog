from rest_framework import routers
from news.views import NewsModelViewset

# app_name = 'news'

router = routers.DefaultRouter()
router.register('', NewsModelViewset, basename='news_api')

urlpatterns = router.urls
