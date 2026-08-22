# doctors/urls.py
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from APIdoctorFinder.views import DoctorViewSet

# Register DRF ViewSets with a router
router = DefaultRouter()
router.register(r"APIdoctorfinder", DoctorViewSet, basename="APIdoctorfinder")

urlpatterns = [
    # Resolves to /api/doctors/ because of the 'api/' prefix in config/urls.py
    path("", include(router.urls)),
]