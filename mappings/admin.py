from django.contrib import admin
from .models import PatientDoctorMapping

# Register your models here.

class PatientDoctorMappingAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'assigned_date', 'is_active')
    list_filter = ('is_active', 'assigned_date', 'doctor__specialization')
    search_fields = ('patient__name', 'doctor__name')
    readonly_fields = ('assigned_date',)
    ordering = ('-assigned_date',)
    