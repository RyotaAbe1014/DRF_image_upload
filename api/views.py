from django.shortcuts import render
from rest_framework import generics
# Create your views here.
from .models import Profile
from .serializers import ProfileSerializer


class ProfileCreateAPIView(generics.CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
