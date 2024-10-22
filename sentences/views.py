from django.shortcuts import render

def sentences(request):
    return render(request, 'sentences/sentences.html')
