from rest_framework.serializers import ModelSerializer, CharField, EmailField, ValidationError
from .models import User, groups_names_list
from django.contrib.auth.models import Group
from django.shortcuts import get_object_or_404
from rest_framework import serializers


class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = ['name']


class UserSerializer(ModelSerializer):
    group = CharField(required=False)
    groups = GroupSerializer(many=True, required=False)
    username = CharField(required=True)
    password = CharField(required=True, min_length=8, write_only=True)

    def validate_group(self, group_name):
        if group_name not in groups_names_list:
            raise Exception('Incorrect group name')
        return group_name

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], password=validated_data['password'])
        user_group = Group.objects.get(name=validated_data['group'])
        user.groups.add(user_group.id)
        user.save()
        return user

    def update(self, user, validated_data):
        user.username = validated_data['username']
        user.password = validated_data['password']
        user_group = Group.objects.get(name=validated_data['group'])
        user.groups.clear()
        user.groups.add(user_group.id)
        user.save()
        return user

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'group', 'groups']





