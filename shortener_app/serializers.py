from rest_framework import serializers
from shortener_app.models import SourceURL


class SourceURLCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SourceURL
        fields = ('url', 'slug')


class SourceURLListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SourceURL
        fields = ('url', 'slug')

