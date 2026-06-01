from django.shortcuts import render, redirect
from EcommerceApp.models import *
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    if request.method=='POST':
        data=request.POST
        uname=data.get("username")
        password=data.get("password")

        user=authenticate(username=uname,password=password)

        if user is not None:
            login(request,user)
            return redirect(product_list)
        return render(request,"index.html",{"err":"invalid credentials: please try again with correct username and password"})
    
    if request.user.is_authenticated:
        return redirect(product_list)
    return render(request,"index.html")

def registration(request):
    if request.method=='POST':
        data=request.POST
        fname=data.get("firstname")
        lname=data.get("lastname")
        uname=data.get("username")
        email=data.get("email")
        password=data.get("password")

        User.objects.create_user(first_name=fname,last_name=lname,username=uname,email=email,password=password)
        return render(request,"registration.html",{"msg":"registration successfull"})
    
    return render(request, "registration.html")


@login_required(login_url="index")
def product_form(request):
    if request.method=='POST':
        data=request.POST
        name=data.get("name")
        price=data.get("price")
        qty=data.get("quantity")
        cat=data.get("category")
        image=data.FILE.get("image")

        category=Category.objects.get(id=cat)

        Product.objects.create(name=name,price=price,quantity=qty,category=category,image=image)
        return render(request,"product_form.html",{"msg":"Product Added Successfully"})

    categories=Category.objects.all()
    return render(request,"product_form.html",{"categories":categories})


@login_required(login_url="index")
def product_list(request):
    products=Product.objects.all()
    return render(request,"product_list.html",{"products":products})
    


    return render(request, "product_list.html")


def logout_user(request):
    logout(request)
    return redirect("index")
