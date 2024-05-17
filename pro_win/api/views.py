from django.shortcuts import render
from .serializers import (AddProjectSerializer, UpdateInformationSerializer, DashboardSerializer)
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


class UpdateList(generics.ListCreateAPIView):
    queryset = ProjectUpdate.objects.all()
    serializer_class = UpdateInformationSerializer

class RetrieveUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProjectUpdate.objects.all()
    serializer_class = UpdateInformationSerializer

class DashboardRetrieve(generics.RetrieveUpdateAPIView):
    queryset = AddProject.objects.all()
    serializer_class = DashboardSerializer



