from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=70)
    rollnumber = models.IntegerField(null=True)
    email = models.CharField(max_length=100)
    age = models.IntegerField(null=True)
    contact = models.IntegerField(null=True)
    course = models.CharField(max_length=10)
   
