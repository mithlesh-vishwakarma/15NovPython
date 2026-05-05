from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Hello from my app</h1>")
    