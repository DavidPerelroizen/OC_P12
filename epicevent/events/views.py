from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import EventSerializer, EventStatusSerializer, ClientSerializer, ContractSerializer
from .models import ClientCustomer, Event, EventStatus, Contract

# Create your views here.


class ContractManagement(ModelViewSet):
    serializer_class = ContractSerializer

    def get_queryset(self):
        return Contract.objects.all()


class ClientManagement(ModelViewSet):
    serializer_class = ClientSerializer

    def get_queryset(self):
        return ClientCustomer.objects.all()


class EventManagement(ModelViewSet):
    serializer_class = EventSerializer

    def get_queryset(self):
        return Event.objects.all()
