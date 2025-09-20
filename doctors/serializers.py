from rest_framework import serializers
from .models import Doctor

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ["name","joined_at","specialization","license_number","salary"]
        