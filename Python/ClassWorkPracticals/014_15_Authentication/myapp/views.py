from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    if request.method == "POST":
        data = request.POST
        uname = data.get("username")
        password = data.get("password")

        user = authenticate(username=uname, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return render(request, "index.html", {"err": "Invalid credentails"})

    if request.user.is_authenticated:
        return redirect("home")
    return render(request, "index.html")


def reg(request):
    if request.method == "POST":
        data = request.POST
        fname = data.get("firstname")
        lname = data.get("lastname")
        uname = data.get("username")
        password = data.get("password")

        # u = User(first_name=fname,last_name=lname,username=uname)
        # u.set_password(password)
        # u.save()

        User.objects.create_user(
            first_name=fname, last_name=lname, username=uname, password=password
        )

        return render(
            request, "registration.html", {"msg": "Registration successfully !!!"}
        )

    return render(request, "registration.html")


@login_required(login_url="index")
def home(request):
    return render(request, "home.html")


def logout_user(request):
    logout(request)
    return redirect("index")
