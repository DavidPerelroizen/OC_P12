from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from .models import User
from .permissions import CanManageUserCreation
# Create your views here.


class UserManagement(ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [CanManageUserCreation]

    def get_queryset(self):
        return User.objects.all()
