from rest_framework import serializers
from .models import Activites,Hoppies,Book,Video
class HoppiesSerializer(serializers. ModelSerializer):
    class Meta:
        model=Hoppies
        fields='__all__'
class BookSerializer(serializers. ModelSerializer):
    class Meta:
        model=Book
        fields='__all__'
class VideoSerializer(serializers. ModelSerializer):
    class Meta:
        model=Video
        fields='__all__'