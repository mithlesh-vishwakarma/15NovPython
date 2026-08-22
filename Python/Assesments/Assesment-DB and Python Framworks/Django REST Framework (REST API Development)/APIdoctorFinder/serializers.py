from rest_framework import serializers
from .models import Doctor


class DoctorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Doctor
        fields = [
            "id",
            "name",
            "specialization",
            "email",
            "phone",
            "experience",
            "clinic_name",
            "city",
            "available",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
        ]

    def validate_name(self, value):
        value = value.strip()

        if len(value) < 3:
            raise serializers.ValidationError(
                "Doctor name must contain at least 3 characters."
            )

        return value

    def validate_experience(self, value):
        if value > 60:
            raise serializers.ValidationError(
                "Experience cannot be greater than 60 years."
            )

        return value