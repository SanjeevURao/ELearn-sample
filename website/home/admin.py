from django.contrib import admin
from .models import Course , Instructor , Interest

admin.site.register(Instructor)
admin.site.register(Course)
admin.site.register(Interest)
