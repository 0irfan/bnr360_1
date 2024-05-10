from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework import generics
from .permissions import IsAdmin
# Create your views here.

class JvCollabList(generics.ListCreateAPIView):
    queryset = JvCollab.objects.all()
    serializer_class = JvCollabSerializer

class JvCollabRetrieve(generics.RetrieveUpdateDestroyAPIView):
    queryset = JvCollab.objects.all()
    serializer_class = JvCollabSerializer
    permission_classes = [IsAdmin]
