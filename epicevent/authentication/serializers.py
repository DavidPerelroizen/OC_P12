from rest_framework.serializers import ModelSerializer, CharField, EmailField
from .models import User
from django.contrib.auth.models import Group


class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = ['name']


class UserSerializer(ModelSerializer):
    authorization_group = GroupSerializer(many=True, required=True)
    username = CharField(required=True)
    password = CharField(required=True, min_length=8, write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], group_id=validated_data['authorization_group'],
                                        password=validated_data['password'])
        return user

    class Meta:
        model = User
        fields = ['username', 'password', 'authorization_group']
