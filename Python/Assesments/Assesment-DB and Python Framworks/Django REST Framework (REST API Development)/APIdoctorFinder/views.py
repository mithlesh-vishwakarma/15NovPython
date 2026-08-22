from django.db import transaction
from rest_framework import filters, viewsets

from .models import Doctor, DoctorProfileUpdateLog
from .serializers import DoctorSerializer


class DoctorViewSet(viewsets.ModelViewSet):

    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

    filter_backends = [
        filters.OrderingFilter,
    ]

    ordering_fields = [
        "name",
        "specialization",
        "experience",
        "city",
        "created_at",
    ]

    ordering = ["name"]

    @transaction.atomic
    def perform_create(self, serializer):
        serializer.save()

    @transaction.atomic
    def perform_update(self, serializer):
        doctor = serializer.save()

        DoctorProfileUpdateLog.objects.create(
            doctor=doctor,
            message="Doctor profile updated"
        )