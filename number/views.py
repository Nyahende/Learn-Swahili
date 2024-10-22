from django.shortcuts import render

def number(request):
    return render(request, 'number/number.html')
