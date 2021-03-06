from django.contrib.auth.models import User
from rest_framework import viewsets
from music_history_api.serializers import *
from music_history_api.models import *

class AlbumViewSet(viewsets.ModelViewSet):
    """
    This creates the Album view
    """
    queryset = album_model.Album.objects.all()
    serializer_class = album_serializer.AlbumSerializer