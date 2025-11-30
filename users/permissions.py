
from rest_framework import permissions

class IsAdmin(permissions.BasePermission):
    """Allows access only to admin users."""
    def has_permission(self, request, view):
        return request.user and request.user.is_staff

class IsRegularUser(permissions.BasePermission):
    """Allows access only to non-admin authenticated users."""
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and not request.user.is_staff