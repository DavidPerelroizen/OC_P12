from django.test import TestCase
import pytest
from .models import Contract, Client, Event, EventStatus
from django.urls import reverse, reverse_lazy
from django.test import Client
from rest_framework.test import APITestCase
from django.contrib.auth.models import Group
from django.shortcuts import get_object_or_404

# Create your tests here.


class TestClientManagement(APITestCase):

    url = 'http://127.0.0.1:8000/api/controller/client_management/'

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_create(self):
        pass

    def test_update(self):
        pass

    def test_delete(self):
        pass
