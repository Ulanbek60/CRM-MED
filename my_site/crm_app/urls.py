from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('departments', DepartmentViewSet)
router.register('services', ServiceViewSet)
router.register('patients', PatientViewSet)
router.register('appointments', AppointmentViewSet)
router.register('medical-records', MedicalRecordViewSet)
router.register('customer-records', CustomerRecordViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
