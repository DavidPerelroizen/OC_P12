from django.test import TestCase
import pytest
from .models import User, administration_group
from django.urls import reverse
from django.test import Client

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
