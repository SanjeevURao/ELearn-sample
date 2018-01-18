from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import  User

class Course(models.Model):
    Name = models.CharField(max_length=100)
    Code = models.CharField(max_length=10)
    Credits = models.IntegerField()
    Semester = models.IntegerField()
    Instructor = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('home:course')

    def __str__(self):
        return self.Name

class Instructor(models.Model):
    Name = models.CharField(max_length=100)
    Phone = models.CharField(max_length=15)
    Email = models.CharField(max_length=100)

    def __str__(self):
        return self.Name

class Interest(models.Model):
    user = models.ForeignKey(User)
    Name = models.CharField(max_length=100)

    def __str__(self):
        return self.Name

    def get_absolute_url(self):
        return reverse('home:index')
