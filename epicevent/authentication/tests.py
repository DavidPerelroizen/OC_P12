from django.test import TestCase
import pytest
from .models import User, administration_group
from django.urls import reverse, reverse_lazy
from django.test import Client
from rest_framework.test import APITestCase
from django.contrib.auth.models import Group
from django.shortcuts import get_object_or_404
from rest_framework.serializers import ValidationError

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

    assert user.description == expected_value


class TestUserManagement(APITestCase):

    url = 'http://127.0.0.1:8000/api/users/user_management/'

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_create(self):
        administration_group, created = Group.objects.get_or_create(name='administrators')
        sales_group, created = Group.objects.get_or_create(name='salesmen')
        support_group, created = Group.objects.get_or_create(name='supporters')

        form_data = {'username': 'david_test', 'password': 'davidou2410', 'group': 'administrators'}
        response = self.client.post(self.url, data=form_data)
        self.assertEqual(response.status_code, 201)
        expected_result = 'david_test, group administrators'
        user = User.objects.all()[0]
        self.assertEqual(user.description, expected_result)

    def test_update(self):
        # Step 1: groups creation
        administration_group, created = Group.objects.get_or_create(name='administrators')
        sales_group, created = Group.objects.get_or_create(name='salesmen')
        support_group, created = Group.objects.get_or_create(name='supporters')

        # Step 2: test user creation
        form_data = {'username': 'david_test', 'password': 'davidou2410', 'group': 'administrators'}
        response = self.client.post(self.url, data=form_data)
        self.assertEqual(response.status_code, 201)
        user_for_update = User.objects.all()[0]
        print(user_for_update.id)

        # Step 3: define target URL for user update and updated data
        url_for_update = f'http://127.0.0.1:8000/api/users/user_management/{user_for_update.id}/'

        form_data_2 = {'username': 'david_test', 'password': 'davidou2410', 'group': 'salesmen'}
        expected_result = 'david_test, group salesmen'

        # Step 4: update the user data
        response = self.client.put(url_for_update, data=form_data_2)

        self.assertEqual(response.status_code, 200)
        updated_user = get_object_or_404(User, id=user_for_update.id)
        self.assertEqual(updated_user.description, expected_result)

    def test_delete(self):
        administration_group, created = Group.objects.get_or_create(name='administrators')
        sales_group, created = Group.objects.get_or_create(name='salesmen')
        support_group, created = Group.objects.get_or_create(name='supporters')

        form_data = {'username': 'david_test', 'password': 'davidou2410', 'group': 'administrators'}
        response = self.client.post(self.url, data=form_data)
        self.assertEqual(response.status_code, 201)

        user_for_deletion = User.objects.all()[0]

        url_for_deletion = f'http://127.0.0.1:8000/api/users/user_management/{user_for_deletion.id}/'
        response = self.client.delete(url_for_deletion)
        self.assertEqual(response.status_code, 204)

    def test_create_user_with_wrong_group_name(self):
        administration_group, created = Group.objects.get_or_create(name='administrators')
        sales_group, created = Group.objects.get_or_create(name='salesmen')
        support_group, created = Group.objects.get_or_create(name='supporters')

        form_data = {'username': 'david_test', 'password': 'davidou2410', 'group': 'administrative'}
        response = self.client.post(self.url, data=form_data)
        self.assertEqual(response.status_code, 400)

