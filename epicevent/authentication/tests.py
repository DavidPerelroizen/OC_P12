from django.test import TestCase
import pytest
from .models import User, administration_group
from django.urls import reverse, reverse_lazy
from django.test import Client
from rest_framework.test import APITestCase

# Create your tests here.


@pytest.mark.django_db
def test_user_model():
    user = User.objects.create_user(username='david_test', password='davidou2410', group_id=administration_group)
    expected_value = 'david_test, group administrators'
    print(str(user))
    assert str(user) == expected_value


@pytest.mark.django_db
def test_user_creation_with_valid_data():
    client = Client()
    url = 'http://127.0.0.1:8000/api/users/sign-up/'
    form_data = {'username': 'david_test', 'password': 'davidou2410', 'group_id': 'administrators'}
    response = client.post(url, data=form_data)
    expected_value = 'david_test, group administrators'
    print(response)
    assert response.status_code == 201
    assert str(response) == expected_value


@pytest.mark.django_db
def test_user_creation_with_invalid_data():
    pass


class TestUserManagement(APITestCase):

    url = 'http://127.0.0.1:8000/api/users/user_management/'

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_create(self):
        form_data = {'username': 'david_test', 'password': 'davidou2410', 'group_id': 'administrators'}
        response = self.client.post(self.url, data=form_data)
        self.assertEqual(response.status_code, 200)
        expected_result = 'david_test, group administrators'
        user = User.objects.get.all()[0]
        self.assertEqual(str(user), expected_result)
