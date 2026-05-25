from django.shortcuts import get_object_or_404, redirect, render
from student_management_system.models import *
# Create your views here.
def index(request):
    return render(request,"index.html")

def add_student(request):
    if request.method=='POST':
        data=request.POST
        name=data.get("name")
        rollnumber=data.get("rollnumber")
        email=data.get("email")
        age = data.get("age")
        contact=data.get("contact")
        course=data.get("course")

        # return render(request,"index.html")
        Student.objects.create(
            name=name,
            rollnumber=rollnumber,
            email=email,
            age=age,
            contact=contact,
            course=course,
        )
        return redirect("display_data")
    return render(request, "index.html")

def display_data(request):
    student_data=Student.objects.all()
    return render(request, "display_data.html", {"student_data":student_data})

def update_data(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == "POST":
        student.name = request.POST.get("name")
        student.rollnumber = request.POST.get("rollnumber")
        student.email = request.POST.get("email")
        student.age = request.POST.get("age")
        student.contact = request.POST.get("contact")
        student.course = request.POST.get("course")
        student.save()
        return redirect("display_data")

    return render(request, "update_student.html", {"student": student})

def delete_data(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect("display_data")
