from rest_framework import serializers
from .models import *


class JvCollabSerializer(serializers.ModelSerializer):
    class Meta:
        model = JvCollab
        field = '__all__'
