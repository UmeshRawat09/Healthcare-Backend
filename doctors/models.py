from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    specialization = models.CharField(max_length=100)
    license_number = models.CharField(max_length=20, unique=True)
    years_of_experience = models.PositiveIntegerField()
    consultation_fee = models.DecimalField(max_digits=10, decimal_places=2)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='doctors')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Dr. {self.name} - {self.specialization}"