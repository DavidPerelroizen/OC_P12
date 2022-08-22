from django.contrib import admin
from .models import ClientCustomer, Contract, Event, EventStatus

# Register your models here.

admin.site.register(ClientCustomer)
admin.site.register(Contract)
admin.site.register(Event)
admin.site.register(EventStatus)
