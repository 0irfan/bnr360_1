from django.shortcuts import render
from .serializers import (AddProjectSerializer, UpdateSerializer)
from .models import (AddProject, ProjectUpdate)
from rest_framework import generics
from .permissions import IsAdmin
# Create your views here.

class AddProjectList(generics.ListCreateAPIView):
    queryset = AddProject.objects.all()
    serializer_class = AddProjectSerializer


class AddProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AddProject.objects.all()
    serializer_class = AddProjectSerializer
    # How can we customize IsAdmin permission..
    permission_classes = [IsAdmin]


class UpdateList(generics.ListCreateAPIView):
    queryset = ProjectUpdate.objects.all()
    serializer_class = UpdateSerializer


class UpdateDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProjectUpdate.objects.all()
    serializer_class = UpdateSerializer
    
