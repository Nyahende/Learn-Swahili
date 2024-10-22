from django.shortcuts import render

def adjectives(request):
    return render(request, 'adjectives/adjectives.html')
