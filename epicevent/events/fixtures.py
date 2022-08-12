import pytest
from django.contrib.auth.models import Group
from authentication import models


def fixture_group_and_user_creation(group_name):
    administration_group, created = Group.objects.get_or_create(name='administrators')
    sales_group, created = Group.objects.get_or_create(name='salesmen')
    support_group, created = Group.objects.get_or_create(name='supporters')

    user = models.User.objects.create_user(username='david_test', password='davidou2410')
    user_group = Group.objects.get(name=group_name)
    user.groups.add(user_group.id)

    return user
