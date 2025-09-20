from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsAdminUser, IsStaffUser
from .models import Patient, PatientDoctorMapping
from .serializers import PatientSerializer, PatientDoctorMappingSerializer, MappingDetailSerializer

class PatientViewSet(viewsets.ModelViewSet):

    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

    def get_permissions(self):

        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            self.permission_classes = [IsAdminUser]
        else:
            self.permission_classes = [IsAuthenticated]

        return super().get_permissions()
    

class PatientDoctorMappingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser | IsStaffUser]
    queryset = PatientDoctorMapping.objects.select_related('patient', 'doctor').all()

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return MappingDetailSerializer
        return PatientDoctorMappingSerializer

    def get_queryset(self):
        queryset = self.queryset
        patient_id = self.request.query_params.get('patient_id')
        if patient_id is not None:
            queryset = queryset.filter(patient__id=patient_id)
        return queryset