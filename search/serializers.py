from rest_framework import serializers
from search.models import Videos

class VideoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Videos
        fields = '__all__'
