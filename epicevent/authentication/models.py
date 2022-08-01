from django.db import models
from django.contrib.auth.models import AbstractUser, Group

# Create your models here.


administration_group, created = Group.objects.get_or_create(name='administrators')
sales_group, created = Group.objects.get_or_create(name='salesmen')
support_group, created = Group.objects.get_or_create(name='supporters')

group_choices = (
    (administration_group.id, 'Administrators'),
    (sales_group.id, 'Salesmen'),
    (support_group.id, 'Supporters')
)


class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='authorization_group',
                                 choices=group_choices)

    USERNAME_FIELD = 'username'
