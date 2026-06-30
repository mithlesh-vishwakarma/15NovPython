from django.shortcuts import render,redirect
from studybuddy.models import *
import os
# Create your views here.

def index(request):
  courses=Course.objects.all()
  return render(request,"index.html",{"courses":courses})


def create(request):
  if request.method=='POST':
    data=request.POST
    profile=request.FILES.get('profile')
    student_id=data.get('student_id')
    first_name=data.get('first_name')
    last_name=data.get('last_name')
    date_of_birth=data.get('date_of_birth')
    email=data.get('email')
    phone=data.get("phone")
    admission_date=data.get('admission_date')
    course=data.get('course')
    courses=Course.objects.get(id=course)
    Student.objects.create(student_id=student_id,first_name=first_name,last_name=last_name,date_of_birth=date_of_birth,email=email,phone=phone,admission_date=admission_date,course=courses)
    return render(request,"index.html",{"msg":"Student details created successfully!!"})

  return redirect("index")

  

def display_student(request):
  students=Student.objects.all()
  return render(request,"display.html",{"students":students})

def delete(request):
  st_id=request.GET.get("id")
  student=Student.objects.get(id=st_id)
  student.delete()
  return redirect("display_student")

def update(request):
  st_id=request.GET.get("id")
  student=Student.objects.get(id=st_id)
  courses=Course.objects.all()
  return render(request,"index.html",{"student":student,"courses":courses})