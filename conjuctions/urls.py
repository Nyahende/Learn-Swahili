from django.urls import path
from . import views

urlpatterns = [
    path('', views.conjuctions, name='conjuctions'), 
   
]
