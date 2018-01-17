from django.template import loader
from django.shortcuts import render , redirect
from django.contrib.auth import authenticate , login
from django.views.generic import View
from .models import Instructor , Course
from django.views.generic.edit import CreateView , UpdateView
from .forms import UserForm
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def index(request):
    template = loader.get_template('home/index.html')
    return render(request,'home/index.html')



def people(request):
    all_people = Instructor.objects.all()
    return render(request , 'home/people.html' , {'people': all_people } )


@login_required(login_url='login')
def CourseView(request):
    course_list = Course.objects.all()
    template = loader.get_template('home/course.html')
    return render(request, 'home/course.html' , {'course':course_list})



class CourseAdd(CreateView):
    model = Course #trying to create a new album
    fields=['Name' , 'Code' , 'Credits' , 'Semester' , 'Instructor']

class CourseUpdate(UpdateView):
    model = Course #trying to create a new album
    fields=['Name' , 'Code' , 'Credits' , 'Semester' , 'Instructor']



class UserFormView(View):
    form_class = UserForm
    template_name = 'home/registration.html'
    #show blank form
    def get(self , request):
        form = self.form_class(None)
        return render(request , self.template_name , {'form' : form})

    #register user
    def post(self , request):
        form = self.form_class(request.POST)

        if form.is_valid():

            #save user info locally and not in the database yet

            user = form.save(commit=False)

            #cleaned data

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            #can not directly update password because it is stored  as a hash value

            user.set_password(password)

            #save info to DB

            user.save()

            user = authenticate(username=username , password=password)

            if user is not None:

                if user.is_active:

                   login(request, user)

                   return redirect('home:index')

        # if fails , then return form

        return render(request , self.template_name , {'form' : form})















