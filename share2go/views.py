from django.shortcuts import render
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import UserSerializer,NoteSerializer
from rest_framework import generics


# Create your views here.
from .models import Profile,Note

class NoteRudAPIView(generics.RetrieveUpdateDestroyAPIView):
    permisson_classes=[IsAuthenticatedOrReadOnly]
    queryset=Note.objects.all()
    serializer_class=NoteSerializer

    # def perform_create(self,validated_data):


class NoteCreateView(generics.ListCreateAPIView):
    permisson_classes=[IsAuthenticatedOrReadOnly]
    queryset=Note.objects.all()
    serializer_class=NoteSerializer



