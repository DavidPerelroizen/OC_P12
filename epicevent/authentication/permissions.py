from rest_framework.permissions import BasePermission


class CanManageUserCreation(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.groups.first().name == 'administrators':
            return True
        else:
            return False
