from django.urls import path
from . import views

urlpatterns = [
    path('', views.adjectives, name='adjectives'), 
   
]
