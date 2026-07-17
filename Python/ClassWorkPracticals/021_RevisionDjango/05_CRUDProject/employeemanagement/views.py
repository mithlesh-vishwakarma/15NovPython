from django.shortcuts import render,redirect
from employeemanagement.models import *
# Create your views here.

def index(request):
    return render(request,"index.html")

def create(request):
    if request.method == "POST":
        data=request.POST
        id = data.get("id")
        name = data.get("name")
        email = data.get("email")
        designation = data.get("designation")

        if id:
            employee = Employee.objects.get(id=id)
            employee.name = name
            employee.email = email
            employee.designation = designation
            employee.save()
            return render(request,"index.html",{"msg":"updated successfully"})
        else:
            Employee.objects.create(name=name,email=email,designation=designation)
            return render(request,"index.html",{"msg":"data saved successfully !!"})
        # return redirect("display")

    return render(request, "index.html")


def display(request):
    employees=Employee.objects.all()
    return render(request, "display.html",{"employees":employees})


def delete(request):
    id=request.GET['id']
    emp=Employee.objects.get(id=id)
    emp.delete()
    return redirect('display')


def update(request):
    id=request.GET['id']
    employee=Employee.objects.get(id=id)
    return render(request,"index.html",{"employee":employee})