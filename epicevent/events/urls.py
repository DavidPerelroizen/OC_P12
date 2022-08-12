from django.urls import path, include
from .views import ContractManagement, ClientManagement, EventManagement, EventStatusManagement
from rest_framework import routers

router = routers.SimpleRouter()

router.register('client_management', ClientManagement, basename='client_management')
router.register('contract_management', ContractManagement, basename='contract_management')
router.register('event_management', EventManagement, basename='event_management')
router.register('eventstatus_management',EventStatusManagement, basename='eventstatus_management')

urlpatterns = [
    path('', include(router.urls)),
]
