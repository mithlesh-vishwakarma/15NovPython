from django.shortcuts import render
from myapp.forms import StudentForm

def stundentData(request):
    form = StudentForm()
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"index.html",{'msg':'Record Inserted Successfully'})
        else:
            return render(request,"index.html",{'msg':'Record Not Inserted'})    
    return render(request,"index.html",{'form':form})
            