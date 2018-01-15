from django.db import models


class Course(models.Model):
    Name = models.CharField(max_length=100)
    Code = models.CharField(max_length=10)
    Credits = models.IntegerField()
    Is_Core = models.BooleanField()
    semester = models.IntegerField()
    Instructor = models.CharField(max_length=100)

class Instructor(models.Model):
    Name = models.CharField(max_length=100)
    Phone = models.CharField(max_length=15)
    Email = models.CharField(max_length=100)

    def __str__(self):
        return self.Name
