from django.contrib import admin
from .models import Patient

# Register your models here.

class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'gender', 'created_by', 'created_at')
    list_filter = ('gender', 'created_at', 'created_by')
    search_fields = ('name', 'email', 'phone')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-created_at',)

admin.site.register(Patient, PatientAdmin)