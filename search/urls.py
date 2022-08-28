from django.urls import path
from search.views import VideosViewset

app_name = 'videos'

urlpatterns = [
    path('videos', VideosViewset.as_view({'get': 'list'}), name='orders') # Only one path with GET allowed
]
