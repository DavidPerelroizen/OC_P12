from django.db import models
from django.contrib.auth.models import AbstractUser, Group

# Create your models here.


administration_group, created = Group.objects.get_or_create(name='administrators')
sales_group, created = Group.objects.get_or_create(name='salesmen')
support_group, created = Group.objects.get_or_create(name='supporters')


class User(AbstractUser):

    def __str__(self):
        return f'{self.username}, group {self.groups.first().name}'
