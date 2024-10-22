from django.shortcuts import render

def adverbs(request):
    return render(request, 'adverbs/adverbs.html')
