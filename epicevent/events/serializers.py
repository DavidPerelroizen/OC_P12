import datetime

from rest_framework.serializers import ModelSerializer, CharField, EmailField, IntegerField, DateTimeField
from .models import ClientCustomer, Event, EventStatus, Contract
from authentication import serializers, models


class EventStatusSerializer(ModelSerializer):
    class Meta:
        model = EventStatus
        fields = ['name', 'date_created', 'date_updated', 'status_is_active']


class ClientSerializer(ModelSerializer):
    first_name = CharField(required=True)
    last_name = CharField(required=True)
    email = EmailField(required=True)
    phone = CharField(required=True)
    mobile = CharField(required=True)
    company_name = CharField(required=True)
    date_created = DateTimeField(required=False)
    date_updated = DateTimeField(required=False)
    sales_contact = serializers.UserSerializer(required=False)
    sales_contact_name = CharField(required=False)

    def create(self, validated_data):
        client_customer = ClientCustomer()
        client_customer.first_name = validated_data['first_name']
        client_customer.last_name = validated_data['last_name']
        client_customer.email = validated_data['email']
        client_customer.phone = validated_data['phone']
        client_customer.mobile = validated_data['mobile']
        client_customer.company_name = validated_data['company_name']
        client_customer.date_created = datetime.datetime.now()
        client_customer.date_updated = datetime.datetime.now()
        client_customer.sales_contact = models.User.objects.get(username=validated_data['sales_contact_name'])
        client_customer.save()
        return client_customer

    def update(self, client_customer, validated_data):
        client_customer.first_name = validated_data['first_name']
        client_customer.last_name = validated_data['last_name']
        client_customer.email = validated_data['email']
        client_customer.phone = validated_data['phone']
        client_customer.mobile = validated_data['mobile']
        client_customer.company_name = validated_data['company_name']
        client_customer.date_updated = datetime.datetime.now()
        client_customer.sales_contact = models.User.objects.get(username=validated_data['sales_contact_name'])
        client_customer.save()
        return client_customer

    class Meta:
        model = ClientCustomer
        fields = ['first_name', 'last_name', 'email', 'phone', 'mobile', 'company_name', 'date_created',
                  'date_updated', 'sales_contact', 'sales_contact_name']


class EventSerializer(ModelSerializer):
    date_created = DateTimeField(required=False)
    date_updated = DateTimeField(required=False)
    attendees = IntegerField(required=True)
    event_date = DateTimeField(required=True)
    notes = CharField(required=True)

    class Meta:
        model = Event
        fields = ['id', 'date_created', 'date_updated', 'event_status', 'attendees', 'event_date', 'notes',
                  'client_customer', 'support_contact']


class ContractSerializer(ModelSerializer):
    class Meta:
        model = Contract
        fields = ['date_created', 'date_updated', 'amount', 'contract_status', 'payment_due_date', 'clientcustomer',
                  'sales_contact']
