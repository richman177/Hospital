from rest_framework import permissions
from .models import Doctor


# class CheckDoctor(permissions.BasePermission):
#     def has_permission(self, request, view):
#         user = request.user
#         if isinstance(user, Doctor) and user.role == 'doctor':
#             return True
#         return False