from django.shortcuts import *
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
        return render(request,"index.html",{"msg": "registration successfully"})

def display_data(request):
    student_data=Student.objects.all()
    return render(request, "display_data.html", {"student_data":student_data})

def delete_data(request):
    id=request.GET.get('id')
    student=Student.objects.get(id=id)
    student.delete()
    return redirect("display_data")