from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render


def index(request):
    template = loader.get_template('home/index.html')
    return render(request,'home/index.html')

def interview(request):
    return HttpResponse("<h1>Welcome to Interview prep page!</h1>")