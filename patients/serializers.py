from rest_framework import serializers
from .models import Patient

class PatientSerilizer(serializers.ModelSerializer):
    create_by = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Patient
        fields = '__all__'
        read_only_fields = ('created_by', 'created_at', 'updated_at')

    def validate_email(self, value):
        if Patient.objects.filter(email=value).exists():
            raise serializers.ValidationError("Patient with this email already exists.")
        return value
        
