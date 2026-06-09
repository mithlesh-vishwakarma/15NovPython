from django.shortcuts import render
from myapp.urls import *

# Create your views here.

def index(request):
    return render(request,'index.html')
    