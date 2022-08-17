from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import EventSerializer, EventStatusSerializer, ClientSerializer, ContractSerializer
from .models import ClientCustomer, Event, EventStatus, Contract
from .permissions import CanUpdateDeleteContracts, CanCreateReadContracts, CanCreateReadClient, CanUpdateDeleteClient,\
    CanCRUDEventStatus

# Create your views here.


class ContractManagement(ModelViewSet):
    serializer_class = ContractSerializer
    permission_classes = [CanUpdateDeleteContracts, CanCreateReadContracts]

    def get_queryset(self):
        return Contract.objects.all()


class ClientManagement(ModelViewSet):
    serializer_class = ClientSerializer
    permission_classes = [CanCreateReadClient, CanUpdateDeleteClient]

    def get_queryset(self):
        return ClientCustomer.objects.all()


class EventManagement(ModelViewSet):
    serializer_class = EventSerializer

    def get_queryset(self):
        return Event.objects.all()


class EventStatusManagement(ModelViewSet):
    serializer_class = EventStatusSerializer
    permission_classes = [CanCRUDEventStatus]

    def get_queryset(self):
        return EventStatus.objects.all()
