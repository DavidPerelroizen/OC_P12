from rest_framework.permissions import BasePermission, SAFE_METHODS


class CanCreateReadContracts(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.method in SAFE_METHODS:
                return True
            elif request.user.groups.first().name == 'salesmen' and request.method == 'POST':
                return True
            else:
                return False
        else:
            return False


class CanUpdateDeleteContracts(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            if request.user.groups.first().name == 'administrators':
                return True
            elif request.user.groups.first().name == 'salesmen' and obj.sales_contact.id == request.user.id:
                return True
            else:
                return False
        else:
            return False


