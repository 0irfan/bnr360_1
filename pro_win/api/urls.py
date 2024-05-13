from django.urls import path
from .views import (AddProjectList,AddProjectDetail,UpdateList,UpdateDetail)

urlpatterns = [
    path('add-project/',AddProjectList.as_view()),
    path('add-project/<init:pk>',AddProjectDetail.as_view()),
    path('update-project',UpdateList.as_view()),
    path('update-project/<init:pk>',UpdateDetail.as_view()),
]
