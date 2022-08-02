from rest_framework.serializers import ModelSerializer
from .models import Client, Event, EventStatus, Contract


class EventStatusSerializer(ModelSerializer):
    class Meta:
        model = EventStatus
        fields = ['name', 'date_created', 'date_updated', 'status_is_active']


class ClientSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'email', 'phone', 'mobile', 'company_name', 'date_created',
                  'date_updated', 'sales_contact']


class EventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = ['date_created', 'date_updated', 'event_status_id', 'attendees', 'event_date', 'notes','client',
                  'support_contact']


class ContractSerializer(ModelSerializer):
    class Meta:
        model = Contract
        fields = ['date_created', 'date_updated', 'amount', 'contract_status', 'payment_due_date', 'client',
                  'sales_contact']