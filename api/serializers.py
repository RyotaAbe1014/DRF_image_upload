from rest_framework import serializers
from .models import Profile
from .models import File


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            'top_image',
        )

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = (
            'file',
        )