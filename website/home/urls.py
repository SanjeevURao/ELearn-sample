from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index , name='index'),
    url(r'^people$' , views.people, name='people'),
    url(r'^register$' , views.UserFormView.as_view() , name='register'),
    url(r'^login/$','django.contrib.auth.views.login', {'template_name': 'home/login.html'} ,name='login'),
    url(r'^course$' , views.CourseView, name='course'),
    url(r'^course/add$' , views.CourseAdd.as_view(), name='addcourse'),
    url(r'^logout/$','django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),
]

