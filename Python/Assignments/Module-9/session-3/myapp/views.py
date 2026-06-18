from django.shortcuts import render
from myapp.urls import *


# Create your views here.

def home(request):
  return render(request,"home.html")