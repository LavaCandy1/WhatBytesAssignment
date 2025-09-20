from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PatientViewSet, PatientDoctorMappingViewSet

router = DefaultRouter()
router.register(r'patients',PatientViewSet)
router.register(r'mappings', PatientDoctorMappingViewSet)

urlpatterns = [
    path('',include(router.urls))
]