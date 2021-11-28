from django.shortcuts import render
from .models import Counter
from .serializers import CounterSerializer
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist

def increment(request):
    counter = Counter.objects.first()
    if counter is None:
        counter = Counter()
    counter.count += 1
    counter.save()
    serializer = CounterSerializer(counter)
    return JsonResponse(serializer.data, status=200)
