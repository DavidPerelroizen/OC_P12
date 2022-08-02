from django.urls import path
from .views import UserCreate


urlpatterns = [
    path('sign-up/', UserCreate.as_view(), name='signup'),
]