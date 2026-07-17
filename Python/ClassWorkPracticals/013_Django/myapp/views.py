from django.shortcuts import render,redirect
from myapp.models import *
# Create your views here.
def index(request):
    return render(request,'index.html')

def reg(request):
    if request.method=='POST':
        data =request.POST
        name= data.get("name")
        email = data.get("email")
        age = data.get("age")
        Student.objects.create(name=name,email=email,age=age)
        # return render(request,"index.html",{"msg":"Registration success !!!"})
        return redirect("display")


def display(request):
    student=Student.objects.all()
    return render(request,'display.html',{"students":student})

def delete_data(request):
    id=request.GET.get('id')
    st = Student.objects.get(id=id)
    st.delete()
    return redirect("display")

def update_data(request):
    id=request.GET.get('id')
    st=Student.objects.get(id=id)
    # print(st)
    # return render(request, "update.html", {"msg": "Data Updated Successfully !!!"})
    if request.method=='POST':
        data = request.POST
        name=data.get("name")
        email=data.get("email")
        age=data.get("age")
        st.name=name
        st.email=email
        st.age=age 
        st.save()
        return render(request, "update.html", {"msg": "Data Updated Successfully !!!"})
    return render(request,"update.html", {"st":st})