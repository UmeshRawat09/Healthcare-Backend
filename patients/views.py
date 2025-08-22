from rest_framework import status, generics, permissions
from rest_framework.response import Response
from patients.models import Patient
from patients.serializers import PatientSerilizer

# Create your views here.
class PatientView(generics.ListCreateAPIView):
    serializer_class = PatientSerilizer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Patient.objects.filter(created_by=self.request.user)
    
    def perform_create(self, serializer):
        return serializer.save(created_by=self.request.user)

class PatientDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PatientSerilizer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Patient.objects.filter(created_by=self.request.user)
    
    def destroy(self, request, *args, **kwargs):
        patient = self.get_object()
        self.perform_destroy(patient)
        return Response({
            'message' : 'Patient deleted successfully'
        }, status=status.HTTP_200_OK)