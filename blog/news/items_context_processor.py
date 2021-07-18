from django.template.context_processors import request
from news.models import News


def items(request):
    titles = News.objects.values_list('title', flat=True)
    return {"items": titles}
