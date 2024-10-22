from django.urls import path
from . import views

urlpatterns = [
    path('', views.pronouns, name='pronouns'), 
   
]
