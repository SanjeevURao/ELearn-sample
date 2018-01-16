from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index , name='index'),
    url(r'^people$' , views.people, name='people'),
    url(r'^register$' , views.UserFormView.as_view() , name='register'),
    url(r'^course$' , views.CourseView, name='course'),
    url(r'^course/add$' , views.CourseAdd.as_view(), name='addcourse'),
]

