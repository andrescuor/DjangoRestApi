from rest_framework import serializers
from .models import *

class HelloSerializer(serializers.Serializer):
    '''Serializar un campo para porbar nuestro APIVIEW'''
    name = serializers.CharField(max_length=10)


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'



