import threading
from django.shortcuts import render
from rest_framework import viewsets

from search.models import Videos
from search.serializers import VideoSerializer
from youtube_polling import poll_youtube


def homepage(request):
    return render(request, 'homepage.html')


class VideosViewset(viewsets.ReadOnlyModelViewSet):
    serializer_class = VideoSerializer

    def get_queryset(self):
        query_params = self.request.query_params

        # Filter the objects to get case insenstive substring match object against the rows in DB.
        queryset = Videos.objects.filter(
            title__contains=query_params.get('title', ''),
            description__contains=query_params.get('description', '')
        ).all().order_by('-published_at')

        return queryset


# Starting poll_youtube as a background thread
thread = threading.Thread(
    target=poll_youtube
)
thread.setDaemon(True)
thread.start()
