from django.http import JsonResponse
from django.shortcuts import redirect
from shortener_app.models import SourceURL
from shortener_app.serializers import SourceURLCreateSerializer, SourceURLListSerializer
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from shortener_app.URLshorterer_services import check_valid_url, check_exists_slug


class SourceUrlCreateView(generics.CreateAPIView):
    serializer_class = SourceURLCreateSerializer

    def post(self, request, *args, **kwargs):
        if not check_valid_url(url=request.data['url']):
            return Response("Resource with this URL don't found.", status=status.HTTP_404_NOT_FOUND)
        if not check_exists_slug(slug=request.data['slug']):
            return Response("Object with this slug already exists.", status=status.HTTP_200_OK)

        return self.create(request, *args, **kwargs)


class SourceUrlListView(generics.ListAPIView):
    serializer_class = SourceURLListSerializer
    queryset = SourceURL.objects.all()


def browse_source_url_view(request, slug):
    try:
        url_source = SourceURL.objects.get(slug=slug)
        return redirect(url_source.url)
    except ObjectDoesNotExist:
        return JsonResponse(status=404, data={
            'status_code': 404,
            'error': 'Resource with this slug was not found.'
    })



