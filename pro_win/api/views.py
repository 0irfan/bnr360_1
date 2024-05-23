from django.shortcuts import render
from .serializers import (AddProjectSerializer, UpdateInformationSerializer, ProjectDashboardSerializer, ProjectManagerSerializer)
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


class ProjectUpdateList(generics.ListCreateAPIView):
    queryset = ProjectUpdate.objects.all()
    serializer_class = UpdateInformationSerializer

class ProjectInfoUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProjectUpdate.objects.all()
    serializer_class = UpdateInformationSerializer

class ProjectManager(generics.RetrieveAPIView):
    queryset = ProjectUpdate.objects.all()
    serializer_class = ProjectManagerSerializer

class DashboardRetrieve(generics.RetrieveAPIView):
    queryset = AddProject.objects.all()
    serializer_class = ProjectDashboardSerializer



