from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
import razorpay

# Create your views here.

def index(request):
    return render(request, "index.html")


def payment(request):
    client = razorpay.Client(auth=("rzp_test_TDH7A8ecMTugCu", "qtRLJZgwYUYB71GD6XEPUgoE"))
    data = { "amount": 50000, "currency": "INR", "receipt": "order_rcptid_11" }
    payment = client.order.create(data=data)
    # Amount is in currency subunits.
    return JsonResponse(payment)


    