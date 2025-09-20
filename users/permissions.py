from rest_framework.permissions import BasePermission

class IsAdminUser(BasePermission):
    # def has_permission(self, request, view):
    def has_permission(self, request):
        return request.user and request.user.is_authenticated and request.user.role == 'ADMIN'

class IsStaffUser(BasePermission):
    # def has_permission(self, request, view):
    def has_permission(self, request):
        return request.user and request.user.is_authenticated and request.user.role == 'STAFF'

'''
need to remove extra test lines
'''