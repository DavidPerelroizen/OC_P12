from django.test import TestCase
import pytest
from .models import User, administration_group

# Create your tests here.


@pytest.mark.django_db
def test_user_model():
    user = User.objects.create_user(username='david_test', password='davidou2410', group_id=administration_group)
    expected_value = 'david_test, group administrators'
    print(str(user))
    assert str(user) == expected_value


def test_user_creation_with_valid_data():
    pass


def test_user_creation_with_invalid_data():
    pass
