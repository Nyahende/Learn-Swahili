from django.urls import path
from . import views

urlpatterns = [
    path('', views.verbs, name='verbs'), 
   
]
