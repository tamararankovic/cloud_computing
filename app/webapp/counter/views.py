from django.shortcuts import render
from .models import Counter
from .serializers import CounterSerializer
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist

def increment(request, id):
    try:
        counter = Counter.objects.get(id = id)
        counter.count += 1
        counter.save()
        serializer = CounterSerializer(counter)
        return JsonResponse(serializer.data, status=200)
    except ObjectDoesNotExist:
        return JsonResponse(None, safe=False, status=400)
