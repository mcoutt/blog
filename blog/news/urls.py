from rest_framework import routers
from news.views import NewsViewset

router = routers.DefaultRouter()
router.register('', NewsViewset)

urlpatterns = router.urls
