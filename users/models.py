from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        STAFF = "STAFF", "Staff"

    phone_number = models.CharField(max_length=15, blank=True)
    role = models.CharField(max_length=50, choices=Role.choices, default=Role.STAFF)
    
