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

# Create your tests here.


class TestClientManagement(APITestCase):

    url = 'http://127.0.0.1:8000/api/controller/client_management/'

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_create(self):
        # Step 1: Group creation
        administration_group, created = Group.objects.get_or_create(name='administrators')
        sales_group, created = Group.objects.get_or_create(name='salesmen')
        support_group, created = Group.objects.get_or_create(name='supporters')

        # Step 2: user creation
        user = models.User.objects.create_user(username='david_test', password='davidou2410')
        user_group = Group.objects.get(id=sales_group.id)
        user.groups.add(user_group.id)
        expected_value = 'david_test, group salesmen'

        self.assertEqual(user.description, expected_value)

        # Step 3: ClientCustomer creation
        form_data = {'first_name': 'first_name_test1', 'last_name': 'last_name_test1', 'email': 'email_test1@test.com',
                     'phone': '0000000', 'mobile': '1111111', 'company_name': 'company_name_test1',
                     'sales_contact_name': 'david_test'}

        response = self.client.post(self.url, data=form_data)

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
        # Step 1: Group creation
        administration_group, created = Group.objects.get_or_create(name='administrators')
        sales_group, created = Group.objects.get_or_create(name='salesmen')
        support_group, created = Group.objects.get_or_create(name='supporters')

        # Step 2: user creation
        user = models.User.objects.create_user(username='david_test', password='davidou2410')
        user_group = Group.objects.get(id=sales_group.id)
        user.groups.add(user_group.id)
        expected_value = 'david_test, group salesmen'

        self.assertEqual(user.description, expected_value)

        # Step 3: ClientCustomer creation
        form_data = {'first_name': 'first_name_test1', 'last_name': 'last_name_test1', 'email': 'email_test1@test.com',
                     'phone': '0000000', 'mobile': '1111111', 'company_name': 'company_name_test1',
                     'sales_contact_name': 'david_test'}

        response = self.client.post(self.url, data=form_data)

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

        # Step 4: ClientCustomer info modification

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
        # Step 1: Group creation
        administration_group, created = Group.objects.get_or_create(name='administrators')
        sales_group, created = Group.objects.get_or_create(name='salesmen')
        support_group, created = Group.objects.get_or_create(name='supporters')

        # Step 2: user creation
        user = models.User.objects.create_user(username='david_test', password='davidou2410')
        user_group = Group.objects.get(id=sales_group.id)
        user.groups.add(user_group.id)
        expected_value = 'david_test, group salesmen'

        self.assertEqual(user.description, expected_value)

        # Step 3: ClientCustomer creation
        form_data = {'first_name': 'first_name_test1', 'last_name': 'last_name_test1', 'email': 'email_test1@test.com',
                     'phone': '0000000', 'mobile': '1111111', 'company_name': 'company_name_test1',
                     'sales_contact_name': 'david_test'}

        response = self.client.post(self.url, data=form_data)

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

        # Step 4: ClientCustomer deletion

        url_for_deletion = self.url + f'{client_created.id}/'
        response = self.client.delete(url_for_deletion)
        self.assertEqual(response.status_code, 204)


class TestEventManagement(APITestCase):

    url = 'http://127.0.0.1:8000/api/controller/event_management/'

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_create(self):
        pass

    def test_update(self):
        pass

    def test_delete(self):
        pass
