from django.shortcuts import render
from django.http import HttpResponse , Http404
from django.template import loader
from django.shortcuts import render
from .models import Instructor

def index(request):
    template = loader.get_template('home/index.html')
    return render(request,'home/index.html')

def people(request):
    all_people = Instructor.objects.all()
    html = ''
    for faculty in all_people:
        url = 'people/'+ str(faculty.id) + '/'
        html += '<a href = "'+url+'" >' + faculty.Name + ' </a><br> '
    return HttpResponse(html)


def detail(request , faculty_id):
    try:
        instructor = Instructor.objects.get(pk=faculty_id)
    except Instructor.DoesNotExist:
        raise Http404("No Instructor Found.")
    return render(request , 'home/details.html' , { 'instructor': instructor })