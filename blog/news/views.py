from rest_framework import viewsets, renderers
from rest_framework.response import Response
from django.shortcuts import render
from news.models import News
from news.serializers import NewsSerializer


def main_page(request):
    return render(request, 'main.html')


class NewsModelViewset(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    renderer_classes = (renderers.JSONRenderer, renderers.TemplateHTMLRenderer)

    def list(self, request, *args, **kwargs):
        response = super(NewsModelViewset, self).list(request, *args, **kwargs)
        if request.accepted_renderer.format == 'html':
            return Response({'data': response.data}, template_name='news-list.html')
        return response
