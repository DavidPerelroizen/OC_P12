from django.db import models
from django.conf import settings

# Create your models here.


class Client(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)
    company_name = models.CharField(max_length=250)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField()
    sales_contact = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sales_client')


class EventStatus(models.Model):
    name = models.CharField(max_length=25)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField()
    status_is_active = models.BooleanField(default=True)


class Event(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField()
    event_status_id = models.ForeignKey(EventStatus, on_delete=models.CASCADE, related_name='event_status')
    attendees = models.IntegerField()
    event_date = models.DateTimeField()
    notes = models.TextField(max_length=1000)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='client_event')
    support_contact = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='support')


class Contract(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField()
    amount = models.FloatField()
    contract_status = models.BooleanField(default=True)
    payment_due_date = models.DateTimeField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='client_contract')
    sales_contact = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sales_contract')