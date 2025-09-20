from django.db import models
from doctors.models import Doctor
from HealthcareBackend import settings

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
    date_of_birth = models.DateField(help_text="Date of birth of patient.")
    phone_number = models.CharField(max_length=15)
    gender = models.CharField(max_length=1,choices=Gender.choices,null=True)
    address = models.TextField()
    medical_record = models.TextField(blank=True)
    assigned_doctors = models.ManyToManyField(Doctor,blank=True)

    def __str__(self):
        return self.name