from rest_framework import serializers

class SendEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True, help_text="User email address to send welcome email")

class SendSMSSerializer(serializers.Serializer):
    phone_number = serializers.CharField(required=True, max_length=20, help_text="Target phone number with country code")
    message = serializers.CharField(required=True, max_length=1600, help_text="SMS message body text")

class PaymentSerializer(serializers.Serializer):
    amount = serializers.DecimalField(max_digits=10, decimal_places=2, required=True, help_text="Payment amount")
    currency = serializers.CharField(max_length=10, default="usd", help_text="Currency code e.g. usd, inr, eur")

class GoogleLoginSerializer(serializers.Serializer):
    id_token = serializers.CharField(required=False, allow_blank=True, help_text="Google OAuth ID Token")
    code = serializers.CharField(required=False, allow_blank=True, help_text="Google Authorization Code")
    email = serializers.EmailField(required=False, allow_blank=True, help_text="User email for login/registration")
