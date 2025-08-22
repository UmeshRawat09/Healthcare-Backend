from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

user = get_user_model()

class Patient(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    name    =   models.CharField(max_length=100)
    email   =   models.EmailField(unique=True)
    phone   =   models.CharField(max_length=15)
    date_of_birth   =   models.DateField()
    gender  =   models.CharField(max_length=1, choices=GENDER_CHOICES)
    address =   models.TextField()
    medical_history =   models.TextField(blank=True, null=True)
    created_by  =   models.ForeignKey(user, on_delete=models.CASCADE, related_name='patients')
    created_at  =   models.DateTimeField(auto_now_add=True)
    updated_at  =   models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name
    