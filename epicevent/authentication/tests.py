from django.test import TestCase
import pytest
from .models import User, administration_group
from django.urls import reverse, reverse_lazy
from django.test import Client
from rest_framework.test import APITestCase
from django.contrib.auth.models import Group

# Create your tests here.


@pytest.mark.django_db
def test_user_model():
    administration_group, created = Group.objects.get_or_create(name='administrators')
    sales_group, created = Group.objects.get_or_create(name='salesmen')
    support_group, created = Group.objects.get_or_create(name='supporters')

    user = User.objects.create_user(username='david_test', password='davidou2410')
    user_group = Group.objects.get(id=1)
    user.groups.add(user_group.id)
    expected_value = 'david_test, group administrators'
    print(str(user))
    assert str(user) == expected_value


class TestUserManagement(APITestCase):

    url = 'http://127.0.0.1:8000/api/users/user_management/'

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_create(self):
        administration_group, created = Group.objects.get_or_create(name='administrators')
        sales_group, created = Group.objects.get_or_create(name='salesmen')
        support_group, created = Group.objects.get_or_create(name='supporters')

        form_data = {'username': 'david_test', 'password': 'davidou2410', 'groups': 'administrators'}
        response = self.client.post(self.url, data=form_data)
        self.assertEqual(response.status_code, 201)
        expected_result = 'david_test, group administrators'
        user = User.objects.all()[0]
        self.assertEqual(str(user), expected_result)
