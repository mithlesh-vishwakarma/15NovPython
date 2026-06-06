from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from myappAJAX.models import *
# Create your views here.

def index(request):
    return render(request,"index.html")


def test(request):
    q=request.GET['q']
    return HttpResponse(f"hello,{q},how are you")

def search(request):
    q=request.GET['q']
    result=""
    # if q=='electric':
    #     result= "<ul><li>option1</li><li>option2</li><li>option3</li></ul>"

    products=Products.objects.filter(name__startswith=q)
    result="<ul>"
    for product in products:
        result+=f"<li>{product.name}</li>"
    result+="</ul>"

    return HttpResponse(result)    

def get_countries(request):
    countries=Country.objects.all()
    return JsonResponse({"data":list(countries.values())})


def get_states(request):
    country_id=request.GET['country_id']

    states=State.objects.filter(country_id=country_id)
    return JsonResponse({"data":list(states.values())})


def get_cities(request):
    state_id = request.GET['state_id']
    cities = City.objects.filter(state_id=state_id)
    return JsonResponse({"data": list(cities.values())})
