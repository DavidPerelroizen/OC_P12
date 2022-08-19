from rest_framework.serializers import ModelSerializer, CharField, EmailField, IntegerField, DateTimeField, FloatField,\
    ValidationError, BooleanField
from .models import ClientCustomer, Event, EventStatus, Contract
from authentication import serializers, models


class EventStatusSerializer(ModelSerializer):
    class Meta:
        model = EventStatus
        fields = ['id', 'name', 'date_created', 'date_updated', 'status_is_active']


class ClientSerializer(ModelSerializer):
    first_name = CharField(required=True)
    last_name = CharField(required=True)
    email = EmailField(required=True)
    phone = CharField(required=True)
    mobile = CharField(required=True)
    company_name = CharField(required=True)
    date_created = DateTimeField(required=False)
    date_updated = DateTimeField(required=False)

    class Meta:
        model = ClientCustomer
        fields = ['id', 'first_name', 'last_name', 'email', 'phone', 'mobile', 'company_name', 'date_created',
                  'date_updated', 'sales_contact']

    def validate_sales_contact(self, sales_contact):
        test_sales_contact = models.User.objects.get(id=sales_contact.id)
        if test_sales_contact.description != f'{test_sales_contact.username}, group salesmen':
            raise ValidationError('The selected sales contact does not belong to the salesmen group')
        return sales_contact


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

    def validate_support_contact(self, support_contact):
        test_support_contact = models.User.objects.get(id=support_contact.id)
        if test_support_contact.description != f'{test_support_contact.username}, group supporters':
            raise ValidationError('The selected sales contact does not belong to the supporters group')
        return support_contact


class ContractSerializer(ModelSerializer):
    date_created = DateTimeField(required=False)
    date_updated = DateTimeField(required=False)
    amount = FloatField(required=True)
    contract_status = BooleanField(required=False)  # Contract not signed = False, Contract signed = True
    payment_due_date = DateTimeField(required=True)

    class Meta:
        model = Contract
        fields = ['id', 'date_created', 'date_updated', 'amount', 'contract_status', 'payment_due_date',
                  'client_customer', 'sales_contact']

    def validate_client_customer(self, client_customer):
        test_client_customer = ClientCustomer.objects.get(id=client_customer.id)
        if test_client_customer is None:
            raise ValidationError('The selected client does not exist')
        return client_customer

    def validate_sales_contact(self, sales_contact):
        test_sales_contact = models.User.objects.get(id=sales_contact.id)
        if test_sales_contact.description != f'{test_sales_contact.username}, group salesmen':
            raise ValidationError('The selected sales contact does not belong to the salesmen group')
        return sales_contact
