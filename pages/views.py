from rest_framework.response import Response
from django.shortcuts import render
from .models import Hoppies,Book,Video
from .serializers import HoppiesSerializer,BookSerializer,VideoSerializer
from rest_framework.decorators import APIView
# from rest_framework import status
# from django.http import JsonResponse
# from django.http import *
# from django import *
from rest_framework import generics
from rest_framework import viewsets



class HoppiesViewSet(viewsets.ModelViewSet):
   queryset=Hoppies.objects.all()
   serializer_class=HoppiesSerializer
class HoppiesViewSet_pk(viewsets.ModelViewSet):
   queryset=Hoppies.objects.all()
   serializer_class=HoppiesSerializer
   lookup_field='id'
class BookViewSet(viewsets.ModelViewSet):
   queryset=Book.objects.all()
   serializer_class=BookSerializer
class VideoViewSet(viewsets.ModelViewSet):
   queryset=Video.objects.all()
   serializer_class=VideoSerializer
   