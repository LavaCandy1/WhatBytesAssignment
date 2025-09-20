from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsAdminUser, IsStaffUser
from .models import Patient, PatientDoctorMapping
from .serializers import PatientSerializer, PatientDoctorMappingSerializer, MappingDetailSerializer
from doctors.serializers import DoctorSerializer
from doctors.models import Doctor

class PatientViewSet(viewsets.ModelViewSet):

    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [IsAdminUser | IsStaffUser]

    def get_permissions(self):

        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            self.permission_classes = [IsAdminUser]
        else:
            self.permission_classes = [IsAuthenticated]

        return super().get_permissions()
    
    def perform_create(self, serializer):
        # for automatically setting the created_by field to the currently logged-in user
        serializer.save(created_by=self.request.user)
    

class PatientDoctorMappingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser | IsStaffUser]
    queryset = PatientDoctorMapping.objects.all()

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
    
class AssignedDoctorsListView(generics.ListAPIView):
    
    serializer_class = DoctorSerializer
    permission_classes = [IsAdminUser | IsStaffUser]

    def get_queryset(self):
        patient_id = self.kwargs['patient_id']
        return Doctor.objects.filter(patientdoctormapping__patient_id=patient_id)