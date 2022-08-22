from rest_framework.permissions import BasePermission, SAFE_METHODS
from .models import ClientCustomer


class ContractsManagementAuthorizations(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.method in SAFE_METHODS:
                return True
            elif request.user.groups.first().name == 'salesmen':
                return True
            elif request.user.groups.first().name == 'administrators' and request.method != 'POST':
                return True
            else:
                return False
        else:
            return False

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


class ClientsManagementAuthorizations(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.method in SAFE_METHODS:
                return True
            elif request.user.groups.first().name == 'salesmen':
                return True
            elif request.user.groups.first().name == 'administrators' and request.method != 'POST':
                return True
            else:
                return False
        else:
            return False

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


class EventStatusManagementAuthorizations(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.user.groups.first().name == 'administrators':
                return True
            else:
                return False
        else:
            return False

    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            if request.user.groups.first().name == 'administrators':
                return True
            else:
                return False
        else:
            return False


class EventManagementAuthorizations(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.method in SAFE_METHODS:
                return True
            elif request.user.groups.first().name == 'salesmen':
                return True
            elif request.user.groups.first().name == 'administrators' and request.method != 'POST':
                return True
            else:
                return False
        else:
            return False

    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            if request.user.groups.first().name == 'administrators':
                return True
            elif request.user.groups.first().name == 'salesmen':
                customer = ClientCustomer.objects.get(id=obj.client_customer.id)
                if customer.sales_contact.id == request.user.id:
                    return True
                else:
                    return False
            elif request.user.groups.first().name == 'supporters' and obj.support_contact.id == request.user.id:
                return True
            else:
                return False
        else:
            return False
