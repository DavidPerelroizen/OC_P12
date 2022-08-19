from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import EventSerializer, EventStatusSerializer, ClientSerializer, ContractSerializer
from .models import ClientCustomer, Event, EventStatus, Contract
from .permissions import CanUpdateDeleteContracts, CanCreateReadContracts, CanCreateReadClient, CanUpdateDeleteClient,\
    CanCRUDEventStatus, CanCreateReadEvent, CanUpdateDeleteEvent

# Create your views here.


class ContractManagement(ModelViewSet):
    serializer_class = ContractSerializer
    permission_classes = [CanUpdateDeleteContracts, CanCreateReadContracts]
    filterset_fields = ['id', 'date_created', 'date_updated', 'amount', 'contract_status', 'payment_due_date',
                        'client_customer', 'sales_contact']

    def get_queryset(self):
        return Contract.objects.all()


class ClientManagement(ModelViewSet):
    serializer_class = ClientSerializer
    permission_classes = [CanCreateReadClient, CanUpdateDeleteClient]
    filterset_fields = ['id', 'first_name', 'last_name', 'email', 'phone', 'mobile', 'company_name', 'date_created',
                        'date_updated', 'sales_contact']

    def get_queryset(self):
        return ClientCustomer.objects.all()


class EventManagement(ModelViewSet):
    serializer_class = EventSerializer
    permission_classes = [CanCreateReadEvent, CanUpdateDeleteEvent]
    filterset_fields = ['id', 'date_created', 'date_updated', 'event_status', 'attendees', 'event_date', 'notes',
                        'client_customer', 'support_contact']

    def get_queryset(self):
        return Event.objects.all()


class EventStatusManagement(ModelViewSet):
    serializer_class = EventStatusSerializer
    permission_classes = [CanCRUDEventStatus]
    filterset_fields = ['id', 'name', 'date_created', 'date_updated', 'status_is_active']

    def get_queryset(self):
        return EventStatus.objects.all()
