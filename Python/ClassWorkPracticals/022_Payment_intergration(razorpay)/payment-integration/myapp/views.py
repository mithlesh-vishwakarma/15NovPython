from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
import razorpay

# Create your views here.

def index(request):
    return render(request, "index.html")


def payment(request):
    amount = request.GET.get('amount')
    try:
        amount_in_rupees = float(amount)
        amount_in_paise = int(amount_in_rupees * 100)
    except (ValueError, TypeError):
        return JsonResponse({"error": "Invalid amount"}, status=400)
        
    client = razorpay.Client(auth=("rzp_test_TDH7A8ecMTugCu", "qtRLJZgwYUYB71GD6XEPUgoE"))
    data = { "amount": amount_in_paise, "currency": "INR", "receipt": "order_rcptid_11" }
    payment = client.order.create(data=data)
    # Return details containing the new order_id and amount
    return JsonResponse(payment)


    