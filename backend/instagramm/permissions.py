from rest_framework.permissions import BasePermission, SAFE_METHODS


class PostPermission(BasePermission):
    def has_permission(self, request, view):
        # return bool(request.user and request.user.is_authenticated)
        if request.method in SAFE_METHODS:
            return True
        if request.user and request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        if request.user and request.user.is_authenticated and obj.user == request.user:
            return True
        return False

