from rest_framework.serializers import ModelSerializer, CharField, EmailField
from .models import User
from django.contrib.auth.models import Group


class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = ['name']


class UserSerializer(ModelSerializer):
    groups = CharField(required=True)
    username = CharField(required=True)
    password = CharField(required=True, min_length=8, write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], password=validated_data['password'])
        user_group = Group.objects.get(name=validated_data['groups'])
        user.groups.add(user_group.id)
        return user

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'groups']
