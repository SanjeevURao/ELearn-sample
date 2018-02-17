from django.template import loader
from django.shortcuts import render , redirect
from django.contrib.auth import authenticate , login
from django.views.generic import View
from .models import Instructor , Course , Interest
from django.views.generic.edit import CreateView , UpdateView , DeleteView
from .forms import UserForm
from django.contrib.auth.decorators import login_required
from .forms import InterestForm
from django.core.urlresolvers import reverse_lazy

@login_required(login_url='login')
def index(request):
    template = loader.get_template('home/index.html')
    interests = Interest.objects.filter(user=request.user)
    return render(request, 'home/index.html', {'interests': interests})


@login_required(login_url='login')
def people(request):
    all_people = Instructor.objects.all()
    return render(request , 'home/people.html' , {'people': all_people } )

def course_details(request):
    all_courses = Course.objects.all()
    return render(request , 'home/details.html' , {'courses': all_courses} )

def CourseGuestView(request):
    course_list = Course.objects.all()
    template = loader.get_template('home/courseguest.html')
    return render(request, 'home/courseguest.html' , {'course':course_list})

@login_required(login_url='login')
def CourseView(request):
    course_list = Course.objects.all()
    template = loader.get_template('home/course.html')
    return render(request, 'home/course.html' , {'course':course_list})

@login_required(login_url='login')
def InterestView(request):
     interests = Interest.objects.filter(user=request.user)
     return render(request, 'home/viewInterest.html' , {'interests':interests})

@login_required(login_url='login')
def AddInterest(request):
    if not request.user.is_authenticated():
        return render(request, 'index/login.html')
    else:
        form = InterestForm(request.POST or None)
        if form.is_valid():
            interest = form.save(commit=False)
            interest.user = request.user

            interest.save()
            interests = Interest.objects.filter(user=request.user)
            return render(request, 'home/index.html', {'interests': interests})
        context = {
                "form": form,
            }
    return render(request, 'home/interest_form.html', context)

class InterestDelete(DeleteView):
    model = Interest
    success_url = reverse_lazy('home:index')

class InterestUpdate(UpdateView):
    model = Interest
    fields = ['Name']


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















