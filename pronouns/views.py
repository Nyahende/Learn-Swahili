from django.shortcuts import render

def pronouns(request):
    return render(request, 'pronouns/pronouns.html')
