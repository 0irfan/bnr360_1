from rest_framework import serializers
from .models import *


class AddProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddProject
        field = '__all__'
