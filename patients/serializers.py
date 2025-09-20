from rest_framework import serializers
from .models import Patient

class PatientSerializer(serializers.ModelSerializer):

    class Meta():
        model = Patient
        fields = ["id","created_by","name","date_of_birth","phone_number","gender","address","medical_record","assigned_doctors"]
