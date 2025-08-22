from rest_framework import status, generics, permissions
from rest_framework.response import Response
from mappings.models import PatientDoctorMapping
from mappings.serializers import PatientDoctorMappingSerializer

# Create your views here.

class MappingView(generics.ListCreateAPIView):
    queryset = PatientDoctorMapping.objects.filter(is_active=True)
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [permissions.IsAuthenticated]

class PatientMapping(generics.ListAPIView):
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        patient_id = self.kwargs('patient')
        return PatientDoctorMapping.objects.filter(
            patient_id=patient_id,
            is_active=True
        )

class MappingDelete(generics.DestroyAPIView):
    queryset = PatientDoctorMapping.objects.all()
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        mapping = self.get_object()
        mapping.is_active = False
        mapping.save()
        return Response({
            'message': 'Mapping removed successfully'
        }, status=status.HTTP_200_OK)