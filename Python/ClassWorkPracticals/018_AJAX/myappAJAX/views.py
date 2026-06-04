from django.shortcuts import render
from myappAJAX.urls import *
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,"index.html")


def test(request):
    q=request.GET['q']
    return HttpResponse(request,f"hello,{q},how are you")