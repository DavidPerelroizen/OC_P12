from rest_framework.serializers import ModelSerializer, CharField, EmailField
from .models import User


class UserSerializer(ModelSerializer):
    username = CharField(required=True)
    password = CharField(required=True, min_length=8, write_only=True)
    group_id = CharField(required=True)

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], group_id=validated_data['group_id'],
                                        password=validated_data['password'])
        return user

    class Meta:
        model = User
        fields = ['username', 'password', 'group_id']
