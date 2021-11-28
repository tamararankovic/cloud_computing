from .models import Song
from .serializers import SongSerializer
from django.http import JsonResponse

def get_all(request):
    songs = Song.objects.all()
    serializer = SongSerializer(songs, many=True)
    return JsonResponse(serializer.data, safe=False, status=200)
