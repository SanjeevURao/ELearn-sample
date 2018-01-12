from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render


def index(request):
    template = loader.get_template('home/index.html')
    a=[1,2,3,4]
    context={'a': a, }
    return render(request,'home/index.html',context)
