from django.shortcuts import render

def verbs(request):
    return render(request, 'verbs/verbs.html')
