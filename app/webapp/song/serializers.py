from django.db.models import fields
from rest_framework import serializers
from .models import Song


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'title', 'performedBy', 'releaseDate', 'rating']