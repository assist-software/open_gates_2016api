from rest_framework import serializers

from .models import AppFile


class AppFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppFile
