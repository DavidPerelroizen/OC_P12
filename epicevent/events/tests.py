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
        administration_group, created = Group.objects.get_or_create(name='administrators')
        sales_group, created = Group.objects.get_or_create(name='salesmen')
        support_group, created = Group.objects.get_or_create(name='supporters')

        user = models.User.objects.create_user(username='david_test', password='davidou2410')
        user_group = Group.objects.get(id=2)
        user.groups.add(user_group.id)
        expected_value = 'david_test, group salesmen'

        self.assertEqual(user.description, expected_value)

        form_data = {'first_name': 'first_name_test1', 'last_name': 'last_name_test1', 'email': 'email_test1@test.com',
                     'phone': '0000000', 'mobile': '1111111', 'company_name': 'company_name_test1',
                     'date_updated': '2022-08-11T11:42:00Z', 'sales_contact': 1}

        response = self.client.post(self.url, data=form_data)
        print(response.data)
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
        pass

    def test_delete(self):
        pass
