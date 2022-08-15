import datetime

from django.test import TestCase
import pytest
from .models import Contract, ClientCustomer, Event, EventStatus
from django.urls import reverse, reverse_lazy
from django.test import Client
from rest_framework.test import APITestCase
from django.contrib.auth.models import Group
from django.shortcuts import get_object_or_404
from authentication import models
from .fixtures import fixture_group_and_user_creation

# Create your tests here.


class TestClientManagement(APITestCase):

    url = 'http://127.0.0.1:8000/api/controller/client_management/'

    form_data = {'first_name': 'first_name_test1', 'last_name': 'last_name_test1', 'email': 'email_test1@test.com',
                 'phone': '0000000', 'mobile': '1111111', 'company_name': 'company_name_test1',
                 'sales_contact_name': 'david_test'}

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_create(self):

        # Step 1: groups and user creation
        user = fixture_group_and_user_creation('salesmen')

        expected_value = 'david_test, group salesmen'

        self.assertEqual(user.description, expected_value)

        # Step 2: ClientCustomer creation

        response = self.client.post(self.url, data=self.form_data)

        self.assertEqual(response.status_code, 201)

        client_created = get_object_or_404(ClientCustomer, id=1)

        self.assertEqual(client_created.first_name, 'first_name_test1')
        self.assertEqual(client_created.last_name, 'last_name_test1')
        self.assertEqual(client_created.email, 'email_test1@test.com')
        self.assertEqual(client_created.phone, '0000000')
        self.assertEqual(client_created.mobile, '1111111')
        self.assertEqual(client_created.company_name, 'company_name_test1')
        self.assertNotEqual(client_created.date_created, '')
        self.assertEqual(client_created.sales_contact.username, 'david_test')

    def test_update(self):
        # Step 1: groups and user creation
        user = fixture_group_and_user_creation('salesmen')

        expected_value = 'david_test, group salesmen'

        self.assertEqual(user.description, expected_value)

        # Step 2: ClientCustomer creation
        response = self.client.post(self.url, data=self.form_data)

        self.assertEqual(response.status_code, 201)

        client_created = ClientCustomer.objects.all()[0]

        self.assertEqual(client_created.first_name, 'first_name_test1')
        self.assertEqual(client_created.last_name, 'last_name_test1')
        self.assertEqual(client_created.email, 'email_test1@test.com')
        self.assertEqual(client_created.phone, '0000000')
        self.assertEqual(client_created.mobile, '1111111')
        self.assertEqual(client_created.company_name, 'company_name_test1')
        self.assertNotEqual(client_created.date_created, '')
        self.assertEqual(client_created.sales_contact.username, 'david_test')

        original_creation_date = client_created.date_created

        # Step 3: ClientCustomer info modification

        form_data_update = {'first_name': 'first_name_test1', 'last_name': 'last_name_test1',
                            'email': 'email_test1@test.com', 'phone': '3333', 'mobile': '4444',
                            'company_name': 'company_name_test1', 'sales_contact_name': 'david_test'}

        url_for_update = self.url + f'{client_created.id}/'

        response_update = self.client.put(url_for_update, data=form_data_update)

        client_updated = get_object_or_404(ClientCustomer, id=client_created.id)

        self.assertEqual(response_update.status_code, 200)

        self.assertEqual(client_updated.first_name, 'first_name_test1')
        self.assertEqual(client_updated.last_name, 'last_name_test1')
        self.assertEqual(client_updated.email, 'email_test1@test.com')
        self.assertEqual(client_updated.phone, '3333')
        self.assertEqual(client_updated.mobile, '4444')
        self.assertEqual(client_updated.company_name, 'company_name_test1')
        self.assertEqual(client_updated.date_created, original_creation_date)
        self.assertNotEqual(client_updated.date_updated, original_creation_date)
        self.assertEqual(client_updated.sales_contact.username, 'david_test')

    def test_delete(self):
        # Step 1: groups and user creation
        user = fixture_group_and_user_creation('salesmen')

        expected_value = 'david_test, group salesmen'

        self.assertEqual(user.description, expected_value)

        # Step 2: ClientCustomer creation
        response = self.client.post(self.url, data=self.form_data)

        self.assertEqual(response.status_code, 201)

        client_created = ClientCustomer.objects.all()[0]

        self.assertEqual(client_created.first_name, 'first_name_test1')
        self.assertEqual(client_created.last_name, 'last_name_test1')
        self.assertEqual(client_created.email, 'email_test1@test.com')
        self.assertEqual(client_created.phone, '0000000')
        self.assertEqual(client_created.mobile, '1111111')
        self.assertEqual(client_created.company_name, 'company_name_test1')
        self.assertNotEqual(client_created.date_created, '')
        self.assertEqual(client_created.sales_contact.username, 'david_test')

        # Step 3: ClientCustomer deletion

        url_for_deletion = self.url + f'{client_created.id}/'
        response = self.client.delete(url_for_deletion)
        self.assertEqual(response.status_code, 204)


class TestEventManagement(APITestCase):

    url = 'http://127.0.0.1:8000/api/controller/event_management/'
    url_client = 'http://127.0.0.1:8000/api/controller/client_management/'

    form_data_client = {'first_name': 'first_name_test1', 'last_name': 'last_name_test1',
                        'email': 'email_test1@test.com', 'phone': '0000000', 'mobile': '1111111',
                        'company_name': 'company_name_test1', 'sales_contact_name': 'david_test'}

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_create(self):
        # Step 1: groups and user creation
        user = fixture_group_and_user_creation('supporters')

        # Step 2: create ClientCustomer
        response = self.client.post(self.url_client, data=self.form_data_client)
        self.assertEqual(response.status_code, 201)
        client_created = ClientCustomer.objects.all()[0]

        # Step 3: create EventStatus
        event_status = EventStatus.objects.get_or_create(name='event_status_name', status_is_active=True)[0]

        # Step 4: create Event
        form_data_event = {'event_status': event_status.id, 'attendees': 200, 'event_date': datetime.datetime.now(),
                           'notes': 'Some notes', 'support_contact': user.id,
                           'client_customer': client_created.id}
        response_event = self.client.post(self.url, data=form_data_event)

        self.assertEqual(response_event.status_code, 201)

        event_created = Event.objects.all()[0]

        self.assertEqual(event_created.event_status.id, form_data_event['event_status'])
        self.assertEqual(event_created.attendees, form_data_event['attendees'])
        self.assertNotEqual(event_created.event_date, '')
        self.assertEqual(event_created.notes, form_data_event['notes'])
        self.assertEqual(event_created.support_contact.id, form_data_event['support_contact'])
        self.assertEqual(event_created.client_customer.id, form_data_event['client_customer'])

    def test_update(self):
        # Step 1: groups and user creation
        user = fixture_group_and_user_creation('supporters')

        # Step 2: create ClientCustomer
        response = self.client.post(self.url_client, data=self.form_data_client)
        self.assertEqual(response.status_code, 201)
        client_created = ClientCustomer.objects.all()[0]

        # Step 3: create EventStatus
        event_status = EventStatus.objects.get_or_create(name='event_status_name', status_is_active=True)[0]

        # Step 4: create Event
        form_data_event = {'event_status': event_status.id, 'attendees': 200, 'event_date': datetime.datetime.now(),
                           'notes': 'Some notes', 'support_contact': user.id,
                           'client_customer': client_created.id}
        response_event = self.client.post(self.url, data=form_data_event)

        self.assertEqual(response_event.status_code, 201)

        event_created = Event.objects.all()[0]

        self.assertEqual(event_created.event_status.id, form_data_event['event_status'])
        self.assertEqual(event_created.attendees, form_data_event['attendees'])
        self.assertNotEqual(event_created.event_date, '')
        self.assertEqual(event_created.notes, form_data_event['notes'])
        self.assertEqual(event_created.support_contact.id, form_data_event['support_contact'])
        self.assertEqual(event_created.client_customer.id, form_data_event['client_customer'])

        # Step 5: update Event
        form_data_update = {'event_status': event_status.id, 'attendees': 400, 'event_date': '2022-09-04T18:37:00Z',
                            'notes': 'Some more notes', 'support_contact': user.id,
                            'client_customer': client_created.id}
        url_for_update = self.url + f'{event_created.id}/'

        response_update = self.client.put(url_for_update, data=form_data_update)

        self.assertEqual(response_update.status_code, 200)
        self.assertEqual(event_created.event_status.id, form_data_update['event_status'])
        self.assertEqual(event_created.attendees, form_data_update['attendees'])
        self.assertEqual(event_created.event_date, form_data_update['event_date'])
        self.assertEqual(event_created.notes, form_data_update['notes'])
        self.assertEqual(event_created.support_contact.id, form_data_update['support_contact'])
        self.assertEqual(event_created.client_customer.id, form_data_update['client_customer'])

    def test_delete(self):
        # Step 1: groups and user creation
        user = fixture_group_and_user_creation('supporters')

        # Step 2: create ClientCustomer
        response = self.client.post(self.url_client, data=self.form_data_client)
        self.assertEqual(response.status_code, 201)
        client_created = ClientCustomer.objects.all()[0]

        # Step 3: create EventStatus
        event_status = EventStatus.objects.get_or_create(name='event_status_name', status_is_active=True)[0]

        # Step 4: create Event
        form_data_event = {'event_status': event_status.id, 'attendees': 200, 'event_date': datetime.datetime.now(),
                           'notes': 'Some notes', 'support_contact': user.id,
                           'client_customer': client_created.id}
        response_event = self.client.post(self.url, data=form_data_event)

        self.assertEqual(response_event.status_code, 201)

        event_created = Event.objects.all()[0]

        self.assertEqual(event_created.event_status.id, form_data_event['event_status'])
        self.assertEqual(event_created.attendees, form_data_event['attendees'])
        self.assertNotEqual(event_created.event_date, '')
        self.assertEqual(event_created.notes, form_data_event['notes'])
        self.assertEqual(event_created.support_contact.id, form_data_event['support_contact'])
        self.assertEqual(event_created.client_customer.id, form_data_event['client_customer'])

        # Step 5: delete Event
        url_for_deletion = self.url + f'{event_created.id}/'
        response = self.client.delete(url_for_deletion)
        self.assertEqual(response.status_code, 204)


class TestContractManagement(APITestCase):

    url_client = 'http://127.0.0.1:8000/api/controller/client_management/'
    url_contract = 'http://127.0.0.1:8000/api/controller/contract_management/'

    form_data_client = {'first_name': 'first_name_test1', 'last_name': 'last_name_test1',
                        'email': 'email_test1@test.com', 'phone': '0000000', 'mobile': '1111111',
                        'company_name': 'company_name_test1', 'sales_contact_name': 'david_test'}

    def test_get(self):
        response = self.client.get(self.url_contract)
        self.assertEqual(response.status_code, 200)

    def test_create(self):
        # Step 1: groups and user creation
        user = fixture_group_and_user_creation('supporters')

        # Step 2: create ClientCustomer
        response = self.client.post(self.url_client, data=self.form_data_client)
        self.assertEqual(response.status_code, 201)
        client_created = ClientCustomer.objects.all()[0]

        # Step 3: create Contract
        form_data_contract = {'amount': 1000,
                              'payment_due_date': datetime.datetime.now(tz=datetime.timezone.utc),
                              'client_customer': client_created.id, 'sales_contact': user.id}
        response_contract = self.client.post(self.url_contract, data=form_data_contract)

        contract_created = Contract.objects.all()[0]

        self.assertEqual(response_contract.status_code, 201)
        self.assertEqual(contract_created.amount, form_data_contract['amount'])
        print(contract_created.payment_due_date)
        print(form_data_contract['payment_due_date'])
        self.assertEqual(contract_created.payment_due_date, form_data_contract['payment_due_date'])
        self.assertEqual(contract_created.sales_contact.id, form_data_contract['sales_contact'])
        self.assertEqual(contract_created.client_customer.id, form_data_contract['client_customer'])
        self.assertEqual(contract_created.contract_status, False)

    def test_update(self):
        pass

    def test_delete(self):
        # Step 1: groups and user creation
        user = fixture_group_and_user_creation('supporters')

        # Step 2: create ClientCustomer
        response = self.client.post(self.url_client, data=self.form_data_client)
        self.assertEqual(response.status_code, 201)
        client_created = ClientCustomer.objects.all()[0]

        # Step 3: create Contract
        form_data_contract = {'amount': 1000, 'payment_due_date': datetime.datetime.now(tz=datetime.timezone.utc),
                              'client_customer': client_created.id, 'sales_contact': user.id}
        response_contract = self.client.post(self.url_contract, data=form_data_contract)

        contract_created = Contract.objects.all()[0]

        self.assertEqual(response_contract.status_code, 201)
        self.assertEqual(contract_created.amount, form_data_contract['amount'])
        self.assertEqual(contract_created.payment_due_date, form_data_contract['payment_due_date'])
        self.assertEqual(contract_created.sales_contact.id, form_data_contract['sales_contact'])
        self.assertEqual(contract_created.client_customer.id, form_data_contract['client_customer'])

        # Step 4: delete Contract
        url_for_deletion = self.url_contract + f'{contract_created.id}/'
        response = self.client.delete(url_for_deletion)
        self.assertEqual(response.status_code, 204)

