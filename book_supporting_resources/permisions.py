from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        return False

    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user.is_superuser
        )