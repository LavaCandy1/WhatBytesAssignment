from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PatientViewSet, PatientDoctorMappingViewSet, AssignedDoctorsListView

router = DefaultRouter()
router.register(r'patients',PatientViewSet)
router.register(r'mappings', PatientDoctorMappingViewSet)

urlpatterns = [
    path('mappings/<int:patient_id>/', AssignedDoctorsListView.as_view(), name='patient-doctors-list'),
    path('',include(router.urls)),
]