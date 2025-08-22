from rest_framework import serializers
from .models import Doctor

class DoctorSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Doctor
        fields = '__all__'
        read_only_fields = ('created_by', 'created_at', 'updated_at')

    def validate_license_number(self, value):
        if Doctor.objects.filter(license_number=value).exists():
            raise serializers.ValidationError("Doctor with this license number already exists.")
        return value
    
    def validate_years_of_experience(self, value):
        if value < 0:
            raise serializers.ValidationError("Years of experience cannot be negative.")
        return value