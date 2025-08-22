from django.contrib import admin
from .models import Doctor

# Register your models here.

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialization', 'license_number', 'years_of_experience', 'consultation_fee')
    list_filter = ('specialization', 'years_of_experience', 'created_at')
    search_fields = ('name', 'email', 'license_number', 'specialization')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-created_at',)

admin.site.register(Doctor, DoctorAdmin)