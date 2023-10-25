from django.contrib import admin
from StudentApp.models import Student, Course
# Register your models here.
admin.site.register(Course) 
admin.site.register(Student)