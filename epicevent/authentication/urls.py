from django.urls import path, include
from .views import UserManagement
from rest_framework import routers

router = routers.SimpleRouter()

router.register('user_management', UserManagement, basename='user_management')

urlpatterns = [
    path('', include(router.urls)),
]
