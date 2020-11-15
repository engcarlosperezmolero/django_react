from django.shortcuts import render
from rest_framework import generics
from .serializers import RoomSerializer
from .models import Room


# Create your views here.
class RoomView(generics.ListAPIView):
    queryset = Room.objects.all()
    # el serializer transforma todos los objetos de mi modelo para convertirlos en algo traducible en un formato tipo JSON.
    serializer_class = RoomSerializer