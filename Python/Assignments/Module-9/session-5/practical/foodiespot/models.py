from django.db.models import ForeignKey
from django.db.models import CharField
from django.db import models

# Create your models here.
class Restaurant(models.Model):
  name=models.CharField(max_length=100)
  location=models.CharField(max_length=100)
  rating=models.FloatField()
  
  def __str__(self):
    return self.name

class Cuisin(models.Model):
  restaurant=models.ForeignKey("Restaurant", on_delete=models.CASCADE)
  name=models.CharField(max_length=20)
  description=models.TextField(max_length=100)
  def __str__(self):
    return self.name