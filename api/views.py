from django.shortcuts import render
from rest_framework import generics
# Create your views here.
from .models import Profile
from .models import File
from .serializers import ProfileSerializer
from .serializers import FileSerializer


class ProfileCreateAPIView(generics.CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class FileCreateAPIView(generics.CreateAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer
