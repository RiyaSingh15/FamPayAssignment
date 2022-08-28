from django.urls import path
from search.views import VideosViewset, homepage

app_name = 'videos'

urlpatterns = [
    path(r'', homepage, name='homepage'),
    path(r'videos', VideosViewset.as_view({'get': 'list'}), name='orders') # Only one path with GET allowed
]
