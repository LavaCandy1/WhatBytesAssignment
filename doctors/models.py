from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    joined_at = models.DateField(auto_now_add=True)
    specialization = models.CharField(max_length=200)
    license_number = models.CharField(max_length=50,unique=True)
    salary = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return f"Dr. {self.name}"