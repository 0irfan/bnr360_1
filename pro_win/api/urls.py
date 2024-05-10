from django.urls import path
from .views import *

urlpatterns = [
    path('/',JvCollabList.as_view()),
    path('/<init:pk>',JvCollabRetrieve.as_view()),
]
