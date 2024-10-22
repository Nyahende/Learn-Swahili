from django.contrib import admin
from django.urls import path, include  # Import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),  
    path('greetings/', include('greetings.urls')),  
    path('conjuctions/', include('conjuctions.urls')),  
    path('adverbs/', include('adverbs.urls')),  
    path('adjectives/', include('adjectives.urls')),  
    path('nouns/', include('nouns.urls')),  
    path('pronouns/', include('pronouns.urls')),  
    path('sentences/', include('sentences.urls')),  
    path('verbs/', include('verbs.urls')),  
]
