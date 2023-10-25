from django.db import models

# Create your models here.
class Course(models.Model):
    cname=models.CharField(max_length=50)
    
    def __str__(self):
        return self.cname
    
class Student(models.Model):
    name=models.CharField(max_length=50)
    course=models.ForeignKey(Course, on_delete=models.CASCADE)
    phno=models.BigIntegerField()
    email=models.CharField(max_length=50)
    age=models.IntegerField()

    def __str__(self):
        return (f'{self.name}, {self.course}')