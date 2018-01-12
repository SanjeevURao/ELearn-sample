from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('home/index.html')
    a=[1,2,3]
    context={
        'a': a,
    }
    return HttpResponse(template.render(context,request))
