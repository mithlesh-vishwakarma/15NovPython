from django.shortcuts import render,redirect
from product_management.models import Product
import os

# Create your views here.
def index(request):
    if request.method=='POST':
        data=request.POST
        name=data.get('name')
        price=data.get('price')
        qty=data.get('qty')
        image=request.FILES.get('image')
        Product.objects.create(name=name,price=price,qty=qty,image=image)
        return render(request,"index.html",{"msg":"Product Added Successfully"})


    return render(request,"index.html")

def display(request):
    products=Product.objects.all()
    return render(request,"display.html",{"products":products})


def delete(request):
    id=request.GET['id']
    product=Product.objects.get(id=id)
    os.remove(product.image.path)
    product.delete()
    return redirect("display")


def update(request):
    id = request.GET["id"]
    product = Product.objects.get(id=id)

    if request.method == "POST":
        data = request.POST
        name = data.get("name")
        price = data.get("price")
        qty = data.get("qty")

        product.name=name
        product.price=price
        product.qty=qty

        if request.FILES:
            os.remove(product.image.path)
            product.image= request.FILES.get("image")
        product.save()

        return render(request,"index.html",{"msg":"Updated Successfully"})   
    return render(request,"index.html",{"product":product})
