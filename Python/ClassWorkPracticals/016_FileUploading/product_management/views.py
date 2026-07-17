from django.shortcuts import *
from product_management.models import *
import os

# Create your views here.
def index(request):
    if request.method == "POST":
        data = request.POST
        cat = data.get("category")
        name = data.get("name")
        price = data.get("price")
        qty = data.get("qty")
        image = request.FILES.get("image")

        category=Category.objects.get(id=cat)

        Product.objects.create(name=name, price=price, qty=qty, image=image,category=category)
        return render(request, "index.html", {"msg": "Registration successfully"})
    
    categories=Category.objects.all()
    return render(request, "index.html", {"categories":categories})

def display(request):
    products=Product.objects.all()
    return render(request,"display.html",{"products":products})

def delete(request):
    id=request.GET['id']
    product = Product.objects.get(id=id)
    os.remove(product.image.path)
    product.delete()
    return redirect("display")


def update(request):
    id = request.GET["id"]
    product = Product.objects.get(id=id)
    categories=Category.objects.all()

    if request.method == "POST":
        data = request.POST
        name = data.get("name")
        price = data.get("price")
        qty = data.get("qty")
        cat=data.get("category")

        product.name = name
        product.price = price
        product.qty = qty
        product.category=Category.objects.get(id=cat)
        
        if request.FILES:
            os.remove(product.image.path)
            product.image = request.FILES.get("image")
        product.save()

        return render(request, "index.html", {"msg": "Update successfully"})

    return render(request, "index.html", {"product": product,"categories":categories})
