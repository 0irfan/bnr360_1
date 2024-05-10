from django.shortcuts import render
from .serializers import AddProjectSerializer
from .models import AddProject
from rest_framework import generics
from .permissions import IsAdmin
# Create your views here.

class AddProjectList(generics.ListCreateAPIView):
    queryset = AddProject.objects.all()
    serializer_class = AddProjectSerializer

class AddProjectRetrieve(generics.RetrieveUpdateDestroyAPIView):
    queryset = AddProject.objects.all()
    serializer_class = AddProjectSerializer
    permission_classes = [IsAdmin]
