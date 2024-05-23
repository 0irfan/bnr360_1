from django.urls import path
from .views import *

urlpatterns = [
    path('add-project/',AddProjectList.as_view()),
    path('add-project/<init:pk>',AddProjectDetail.as_view()),
    path('update-project',ProjectUpdateList.as_view()),
    path('update-project/<init:pk>',ProjectInfoUpdate.as_view()),    
    path('project-dashboard/<init:pk>',DashboardRetrieve.as_view()),
    path('project-manager/<init:pk>',ProjectManager.as_view()),    
]
