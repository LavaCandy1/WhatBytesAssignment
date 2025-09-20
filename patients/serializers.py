from rest_framework import serializers
from .models import Patient, PatientDoctorMapping
from doctors.serializers import DoctorSerializer

class PatientSerializer(serializers.ModelSerializer):

    class Meta():
        model = Patient
        fields = ["id","created_by","name","date_of_birth","phone_number","gender","address","medical_record","assigned_doctors"]

class PatientNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'name']

class MappingDetailSerializer(serializers.ModelSerializer):
    
    patient = PatientNameSerializer(read_only=True)
    doctor = DoctorSerializer(read_only=True)

    class Meta:
        model = PatientDoctorMapping
        fields = ['id', 'patient', 'doctor', 'assigned_at']

class PatientDoctorMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientDoctorMapping
        fields = ['id', 'patient', 'doctor']