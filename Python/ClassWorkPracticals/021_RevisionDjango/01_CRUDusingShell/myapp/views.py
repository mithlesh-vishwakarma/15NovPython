from myapp.models import Student
from datetime import date
from django.shortcuts import render
from myapp.urls import *
# Create your views here.

def index(request):
  return render(request,"index.html")

def add_student(request):
  if request.method=='POST':
    data=request.POST
    name=data.get("name")
    age=data.get("age")
    email=data.get("email")
    Student.objects.create(name=name,age=age,email=email)
    return render(request,"index.html", {"msg":"Registration Successfully...!!"})


  return render(request,"index.html") 