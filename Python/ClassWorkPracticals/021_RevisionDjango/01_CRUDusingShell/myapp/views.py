from myapp.models import Student
from datetime import date
from django.shortcuts import render,redirect
from myapp.urls import *
# Create your views here.

def index(request):
  return render(request,"index.html")

def add_student(request):
  if request.method=='POST':
    data=request.POST
    id=data.get("id")
    name=data.get("name")
    age=data.get("age")    
    email=data.get("email")

    if id:
      student=Student.objects.get(id=id)
      student.name=name
      student.age=age
      student.email=email
      student.save()
      return render(request,"index.html", {"msg":"updated Successfully...!!"})

    else:
      Student.objects.create(name=name,age=age,email=email)
      return render(request,"index.html", {"msg":"Registration Successfully...!!"})

  return render(request,"index.html") 



def display(request):
  students=Student.objects.all()
  return render(request,"display.html",{"students":students})


def delete(request):
  student_id=request.GET.get("id")
  student=Student.objects.get(id=student_id)
  student.delete()
  return redirect("display")

def update(request):
  student_id=request.GET.get("id")
  student=Student.objects.get(id=student_id)
  return render(request,"index.html",{"student":student})
  