from rest_framework.permissions import (IsAdminUser,IsAuthenticated)

class IsAdmin(IsAdminUser):
    def has_permission(self, request, view):
        return request.user.is_staff
