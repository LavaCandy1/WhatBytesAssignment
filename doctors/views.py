from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Doctor
from .serializers import DoctorSerializer
from users.permissions import IsAdminUser

class DoctorViewSet(viewsets.ModelViewSet):

    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

    def get_permissions(self):
        
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            self.permission_classes = [IsAdminUser]
        else:
            self.permission_classes = [IsAuthenticated]
        
        return super().get_permissions()
    

