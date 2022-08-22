from django.db import models
from django.conf import settings

# Create your models here.


class ClientCustomer(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)
    company_name = models.CharField(max_length=250)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    sales_contact = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sales_client')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class EventStatus(models.Model):
    name = models.CharField(max_length=25)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    status_is_active = models.BooleanField(default=True)


class Event(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    event_status = models.ForeignKey(EventStatus, on_delete=models.CASCADE, related_name='status_event')
    attendees = models.IntegerField()
    event_date = models.DateTimeField()
    notes = models.TextField(max_length=1000)
    client_customer = models.ForeignKey(ClientCustomer, on_delete=models.CASCADE, related_name='client_event')
    support_contact = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='support')

    def __str__(self):
        return f'''
        Event for customer {self.client_customer}, managed by {self.support_contact.description}, will take place on
        {self.event_date}, with {self.attendees} attendees.
        Notes: {self.notes}
        date_created : {self.date_created}
        date_updated : {self.date_updated}
        event_status: {self.event_status}
        '''


class Contract(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    amount = models.FloatField()
    contract_status = models.BooleanField(default=False)  # Contract not signed = False, Contract signed = True
    payment_due_date = models.DateTimeField()
    client_customer = models.ForeignKey(ClientCustomer, on_delete=models.CASCADE, related_name='client_contract')
    sales_contact = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                      related_name='sales_contract')

    def __str__(self):
        return f'Contract n°{self.id}, client company {self.client_customer}, contract status {self.contract_status}'
