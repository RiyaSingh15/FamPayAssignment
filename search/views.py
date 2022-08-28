from rest_framework import viewsets

from search.models import Videos
from search.serializers import VideoSerializer


class VideosViewset(viewsets.ReadOnlyModelViewSet):
    serializer_class = VideoSerializer

    def get_queryset(self):
        query_params = self.request.query_params

        queryset = Videos.objects.filter(
            title__contains=query_params.get('title', ''),
            description__contains=query_params.get('description', '')
        ).all().order_by('-published_at')

        return queryset
