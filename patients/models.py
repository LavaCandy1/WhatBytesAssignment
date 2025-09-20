from django.db import models
from doctors.models import Doctor
from HealthcareBackend import settings

class PatientDoctorMapping(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    assigned_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('patient', 'doctor')

    def __str__(self):
        return f"{self.patient.name} - Dr. {self.doctor.name}"

class Patient(models.Model):
    class Gender(models.TextChoices):
        MALE = "M", "Male"
        FEMALE = "F", "Female"
        OTHER = "O", "Other"

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='created_patients'
    )

    name = models.CharField(max_length=100)
    date_of_birth = models.DateField(help_text="Date of birth of patient.",blank=True,null=True)
    phone_number = models.CharField(max_length=15,blank=True)
    gender = models.CharField(max_length=1,choices=Gender.choices,null=True)
    address = models.TextField(blank=True)
    medical_record = models.TextField(blank=True)
    assigned_doctors = models.ManyToManyField(Doctor,through=PatientDoctorMapping,blank=True)

    def __str__(self):
        return self.name