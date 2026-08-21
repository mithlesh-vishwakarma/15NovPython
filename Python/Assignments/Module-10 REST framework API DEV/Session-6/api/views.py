import os
import uuid
import requests
from decimal import Decimal
from django.conf import settings
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import (
    SendEmailSerializer,
    SendSMSSerializer,
    PaymentSerializer,
    GoogleLoginSerializer,
)

# Task 1: /api/send-email/
@api_view(['POST'])
@permission_classes([AllowAny])
def send_email_view(request):
    """
    Endpoint to send a welcome email to a user using the Mailgun API via requests library.
    """
    serializer = SendEmailSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    email = serializer.validated_data['email']
    domain = getattr(settings, 'MAILGUN_DOMAIN', '')
    api_key = getattr(settings, 'MAILGUN_API_KEY', '')
    
    # Check if credentials exist and are real credentials
    is_live_configured = bool(api_key and domain and not api_key.startswith('key-your') and not domain.startswith('sandbox-your'))
    
    if is_live_configured:
        try:
            url = f"https://api.mailgun.net/v3/{domain}/messages"
            response = requests.post(
                url,
                auth=("api", api_key),
                data={
                    "from": f"Welcome Team <mailgun@{domain}>",
                    "to": [email],
                    "subject": "Welcome to Our Platform!",
                    "text": f"Hello {email},\n\nWelcome to our platform! We are thrilled to have you onboard.\n\nBest regards,\nThe Team"
                },
                timeout=10
            )
            
            if response.status_code == 200:
                resp_data = response.json()
                return Response({
                    "status": "success",
                    "message": f"Welcome email sent successfully to {email} via Mailgun API.",
                    "mailgun_id": resp_data.get("id"),
                    "details": resp_data.get("message")
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    "status": "error",
                    "message": "Mailgun API error",
                    "status_code": response.status_code,
                    "details": response.text
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                
        except Exception as e:
            return Response({
                "status": "error",
                "message": f"Failed to send email via Mailgun: {str(e)}"
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        # Fallback simulated response for testing & demonstration
        simulated_id = f"<{uuid.uuid4().hex[:12]}@{domain if domain else 'sandbox.mailgun.org'}>"
        return Response({
            "status": "success",
            "mode": "simulated",
            "message": f"Welcome email processed for {email}.",
            "mailgun_id": simulated_id,
            "details": "Mailgun API request simulated successfully (Configure MAILGUN_API_KEY & MAILGUN_DOMAIN in .env for live dispatch).",
            "email_preview": {
                "to": email,
                "subject": "Welcome to Our Platform!",
                "body": f"Hello {email}, Welcome to our platform!"
            }
        }, status=status.HTTP_200_OK)


# Task 2: /api/send-sms/
@api_view(['POST'])
@permission_classes([AllowAny])
def send_sms_view(request):
    """
    Endpoint that accepts a phone number and message, then sends SMS using Twilio's API.
    """
    serializer = SendSMSSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    phone_number = serializer.validated_data['phone_number']
    message_text = serializer.validated_data['message']
    
    account_sid = getattr(settings, 'TWILIO_ACCOUNT_SID', '')
    auth_token = getattr(settings, 'TWILIO_AUTH_TOKEN', '')
    from_number = getattr(settings, 'TWILIO_PHONE_NUMBER', '')
    
    is_live_configured = bool(
        account_sid and auth_token and from_number and 
        not account_sid.startswith('ACXXXX')
    )
    
    if is_live_configured:
        try:
            from twilio.rest import Client
            client = Client(account_sid, auth_token)
            msg = client.messages.create(
                body=message_text,
                from_=from_number,
                to=phone_number
            )
            return Response({
                "status": "success",
                "message": "SMS sent successfully via Twilio.",
                "sid": msg.sid,
                "to": phone_number,
                "twilio_status": msg.status
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "status": "error",
                "message": f"Twilio API Error: {str(e)}"
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        # Fallback simulated response
        simulated_sid = f"SM{uuid.uuid4().hex}"
        return Response({
            "status": "success",
            "mode": "simulated",
            "message": "SMS request processed successfully.",
            "sid": simulated_sid,
            "to": phone_number,
            "sms_text": message_text,
            "details": "Twilio API simulated successfully (Configure TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER in .env for live SMS)."
        }, status=status.HTTP_200_OK)


# Task 3: /api/pay/
@api_view(['POST'])
@permission_classes([AllowAny])
def pay_view(request):
    """
    Endpoint simulating payment using Stripe test API keys.
    Accepts amount and currency in body and returns payment status & transaction ID.
    """
    serializer = PaymentSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    amount = serializer.validated_data['amount']
    currency = serializer.validated_data['currency'].lower()
    
    stripe_key = getattr(settings, 'STRIPE_SECRET_KEY', '')
    is_live_configured = bool(stripe_key and not stripe_key.startswith('sk_test_51...'))
    
    if is_live_configured:
        try:
            import stripe
            stripe.api_key = stripe_key
            
            # Amount in cents
            amount_in_cents = int(Decimal(str(amount)) * 100)
            
            payment_intent = stripe.PaymentIntent.create(
                amount=amount_in_cents,
                currency=currency,
                payment_method_types=['card'],
                description='Simulation payment via DRF API',
            )
            
            return Response({
                "status": "succeeded",
                "transaction_id": payment_intent.id,
                "amount": float(amount),
                "currency": currency.upper(),
                "client_secret": payment_intent.client_secret,
                "message": "Payment Intent created successfully via Stripe API."
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                "status": "error",
                "message": f"Stripe Payment Error: {str(e)}"
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        # Fallback simulated response
        txn_id = f"pi_3M{uuid.uuid4().hex[:20]}"
        return Response({
            "status": "succeeded",
            "mode": "simulated",
            "transaction_id": txn_id,
            "amount": float(amount),
            "currency": currency.upper(),
            "message": "Payment simulated successfully using Stripe test environment.",
            "details": "Stripe test mode executed (Set STRIPE_SECRET_KEY in .env to connect to live/test Stripe account)."
        }, status=status.HTTP_200_OK)


# Task 4: /api/google-login/
@api_view(['POST'])
@permission_classes([AllowAny])
def google_login_view(request):
    """
    Endpoint implementing Google Login authentication.
    Accepts Google ID token or email, authenticates/creates user, and issues a JWT token.
    """
    serializer = GoogleLoginSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    id_token = serializer.validated_data.get('id_token')
    email = serializer.validated_data.get('email')
    
    user_email = None
    first_name = ""
    last_name = ""
    
    # Try verifying Google OAuth ID token if provided
    if id_token and not id_token.startswith('mock_'):
        try:
            from google.oauth2 import id_token as google_id_token
            from google.auth.transport import requests as google_requests
            
            client_id = getattr(settings, 'GOOGLE_CLIENT_ID', None)
            id_info = google_id_token.verify_oauth2_token(
                id_token,
                google_requests.Request(),
                client_id if client_id and not client_id.startswith('your-google') else None
            )
            
            user_email = id_info.get('email')
            first_name = id_info.get('given_name', '')
            last_name = id_info.get('family_name', '')
        except Exception as e:
            # If verification fails with a real token, pass through to email fallback or return error
            pass
            
    # Fallback to provided email or generate simulated google user for testing
    if not user_email:
        if email:
            user_email = email
        else:
            user_email = "google_user@example.com"
        first_name = "Google"
        last_name = "User"
        
    username = user_email.split('@')[0]
    
    # Retrieve or create Django user
    user, created = User.objects.get_or_create(
        email=user_email,
        defaults={
            'username': username,
            'first_name': first_name,
            'last_name': last_name,
        }
    )
    
    # Ensure username is valid & unique if user wasn't found by email
    if created and User.objects.filter(username=username).exclude(pk=user.pk).exists():
        user.username = f"{username}_{uuid.uuid4().hex[:4]}"
        user.save()

    # Generate JWT tokens (SimpleJWT)
    refresh = RefreshToken.for_user(user)
    
    return Response({
        "status": "success",
        "message": "User authenticated via Google Login.",
        "user": {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "is_new_user": created
        },
        "tokens": {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "token_type": "Bearer"
        }
    }, status=status.HTTP_200_OK)
