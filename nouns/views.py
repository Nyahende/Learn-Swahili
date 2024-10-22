from django.shortcuts import render

def nouns(request):
    return render(request, 'nouns/nouns.html')
