from django.urls import path
from . import views

urlpatterns = [
    path('', views.greetings, name='greetings'), 
    path('submit-contact-form/', views.submit_contact_form, name='submit_contact_form'),
   
]
