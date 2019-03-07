from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    contextDic = {
        'boldmessage': 'i am context',

    }
    return render(request, 'rango/index.html', context=contextDic)

def about(request):
    context = {
        'name': 'hanzheng',
    }
    return render(request, 'rango/about.html', context=context)