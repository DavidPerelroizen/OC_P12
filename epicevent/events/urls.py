from django.urls import path, include
from .views import ContractManagement, ClientManagement, EventManagement
from rest_framework import routers

router = routers.SimpleRouter()

router.register('client_management', ClientManagement, basename='client_management')
router.register('contract_management', ContractManagement, basename='contract_management')
router.register('event_management', EventManagement, basename='event_management')

urlpatterns = [
    path('', include(router.urls)),
]