from django.db import models

# Create your models here.

class Student(models.Model) : 
    student_name = models.CharField(max_length=30)
    student_address = models.CharField(max_length=100)
    student_age = models.IntegerField()
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    
    class Meta:
        db_table = 'student_tb'

