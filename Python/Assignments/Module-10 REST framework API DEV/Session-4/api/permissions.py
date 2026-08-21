from rest_framework import permissions

# Custom permission class for Task 4
class IsPremiumUser(permissions.BasePermission):
    """
    Custom permission to only allow users with is_premium=True to access the endpoint.
    """
    def has_permission(self, request, view):
        return bool(
            request.user and 
            request.user.is_authenticated and 
            request.user.is_premium
        )
