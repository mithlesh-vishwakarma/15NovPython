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
        image=request.FILES.get("image")

        category=None
        if cat and cat != "0":
            try:
                category=Category.objects.get(id=cat)
            except (Category.DoesNotExist, ValueError):
                pass

        Product.objects.create(name=name,price=price,qty=qty,category=category,image=image)
        categories=Category.objects.all()
        return render(request,"product_form.html",{"msg":"Product Added Successfully", "categories":categories})

    categories=Category.objects.all()
    return render(request,"product_form.html",{"categories":categories})


@login_required(login_url="index")
def product_list(request):
    products=Product.objects.all()
    return render(request,"product_list.html",{"products":products})
    

@login_required(login_url="index")
def edit_product(request, pk):
    try:
        product = Product.objects.get(id=pk)
    except Product.DoesNotExist:
        return redirect(product_list)

    if request.method == 'POST':
        data = request.POST
        name = data.get("name")
        price = data.get("price")
        qty = data.get("quantity")
        cat = data.get("category")
        image = request.FILES.get("image")

        category = None
        if cat and cat != "0":
            try:
                category = Category.objects.get(id=cat)
            except (Category.DoesNotExist, ValueError):
                pass

        product.name = name
        product.price = price
        product.qty = qty
        product.category = category
        if image:
            product.image = image
        product.save()

        categories = Category.objects.all()
        return render(request, "product_form.html", {
            "msg": "Product Updated Successfully",
            "product": product,
            "categories": categories
        })

    categories = Category.objects.all()
    return render(request, "product_form.html", {
        "product": product,
        "categories": categories
    })


@login_required(login_url="index")
def delete_product(request, pk):
    try:
        product = Product.objects.get(id=pk)
        product.delete()
    except Product.DoesNotExist:
        pass
    return redirect(product_list)


def logout_user(request):
    logout(request)
    return redirect("index")
