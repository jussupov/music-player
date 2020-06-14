from rest_framework.generics import ListAPIView
from .serializers import SongSerializer
from .models import Song

class SongView(ListAPIView):
    serializer_class = SongSerializer
    queryset = Song.objects.all()
