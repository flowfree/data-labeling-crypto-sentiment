from django.conf import settings
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from djangorestframework_camel_case.render import (
    CamelCaseJSONRenderer,
    CamelCaseBrowsableAPIRenderer,
)

from .models import Site, News
from .serializers import SiteSerializer, NewsSerializer
from .scraper import ScraperError


if settings.DEBUG:
    renderers = [CamelCaseJSONRenderer, CamelCaseBrowsableAPIRenderer]
else:
    renderers = [CamelCaseJSONRenderer]


class SiteViewSet(ModelViewSet):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer
    renderer_classes = renderers


class NewsViewSet(ModelViewSet):
    queryset = News.objects.all().order_by('-pk')
    serializer_class = NewsSerializer
    renderer_classes = renderers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['url', 'site', 'sentiment']

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except ScraperError as e:
            return Response({'error': [f'{e}']}, status=500)
