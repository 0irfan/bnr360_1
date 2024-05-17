from django.urls import path
from .views import (AddProjectList,AddProjectDetail,UpdateList, RetrieveUpdate, DashboardRetrieve)

urlpatterns = [
    path('add-project/',AddProjectList.as_view()),
    path('add-project/<init:pk>',AddProjectDetail.as_view()),
    path('update-project',UpdateList.as_view()),
    path('update-project/<init:pk>',RetrieveUpdate.as_view()),
    path('project-dashboard/<init:pk>',DashboardRetrieve.as_view()),
]
