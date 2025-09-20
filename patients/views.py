from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsAdminUser
from .models import Patient
from .serializers import PatientSerializer

class PatientViewSet(viewsets.ModelViewSet):

    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

    def get_permissions(self):

        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            self.permission_classes = [IsAdminUser]
        else:
            self.permission_classes = [IsAuthenticated]

        return super().get_permissions()