from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index , name='index'),
    url(r'^people$' , views.people, name='people'),
    url(r'^people/(?P<faculty_id>[0-9]+)/$' , views.detail, name='detail'),
]

