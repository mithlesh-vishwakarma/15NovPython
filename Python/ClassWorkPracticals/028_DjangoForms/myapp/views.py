from django.shortcuts import redirect
from django.shortcuts import render
from myapp.forms import StudentForm
from myapp.models import Student

def stundentData(request):
    form = StudentForm()
    students = Student.objects.all()
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("stundentData")
    
    return render(request,"index.html",{'form':form,'students':students})


def delete(request):
    sid = request.GET['id']
    Student.objects.filter(id=sid).delete()
    return redirect("stundentData")


def update(request):
    sid = request.GET['id']
    student = Student.objects.get(id=sid)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
    else:
        form = StudentForm(instance=student)
        
    return render(request, "index.html", {'form': form, 'student': student})
