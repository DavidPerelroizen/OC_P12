from django.contrib.auth.models import AbstractUser, Group


# Create your models here.

'''
Instruction for readme: comment the four lines below before making the first migration.
After the first migration, de-comment them and migrate.
'''
# Groups creation
administration_group, created = Group.objects.get_or_create(name='administrators')
sales_group, created = Group.objects.get_or_create(name='salesmen')
support_group, created = Group.objects.get_or_create(name='supporters')

groups_names_list = [administration_group.name, sales_group.name, support_group.name]


class User(AbstractUser):

    @property
    def description(self):
        return f'{self.username}, group {self.groups.first().name}'
