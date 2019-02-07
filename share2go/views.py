from django.shortcuts import render
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import UserSerializer,NoteSerializer
from rest_framework import generics
from django.contrib.auth.models import User


# Create your views here.
from .models import Profile,Note

class NoteRudAPIView(generics.RetrieveUpdateDestroyAPIView):
    permisson_classes=[IsAuthenticatedOrReadOnly]
    queryset=Note.objects.all()
    serializer_class=NoteSerializer

class NoteCreateView(generics.CreateAPIView):
    permisson_classes=[IsAuthenticatedOrReadOnly]
    serializer_class=NoteSerializer
    queryset=Note.objects.all()
    # def get_queryset(self):
    #     receiver=self.kwargs['username']

class NoteListView(generics.ListAPIView):
    #permisson_classes=[IsAuthenticatedOrReadOnly]
    permisson_classes=None
    serializer_class=NoteSerializer
    queryset=Note.objects.all()

    def get_queryset(self):
        # return Note.objects.filter(receiver__profile__user__id=self.request.user.id)
        return Note.objects.all()



