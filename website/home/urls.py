from django.conf.urls import url
from . import views
from django.contrib.auth.views import login , logout


urlpatterns = [
    url(r'^$', views.index , name='index'),
    url(r'^people$' , views.people, name='people'),
    url(r'^details$', views.course_details, name='details'),
    url(r'^register$' , views.UserFormView.as_view() , name='register'),
    url(r'^login/$',login, {'template_name': 'home/login.html'} ,name='login'),
    url(r'^course$' , views.CourseView, name='course'),
    url(r'^courseguest$', views.CourseGuestView, name='courseguest'),
    url(r'^interest/add$' , views.AddInterest, name='addinterest'),
    url(r'^interests$', views.InterestView , name='viewinterest'),
    url(r'^interests/(?P<pk>[0-9]+)/delete/$', views.InterestDelete.as_view(), name='deleteinterest'),
    url(r'^interests/(?P<pk>[0-9]+)/$', views.InterestUpdate.as_view(), name='updateinterest'),
    url(r'^logout/$',logout, {'next_page': '/'}, name='logout'),
]



