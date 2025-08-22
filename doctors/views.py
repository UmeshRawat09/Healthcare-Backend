from rest_framework import status, generics, permissions
from rest_framework.response import Response
from doctors.models import Doctor
from doctors.serializers import DoctorSerializer
# Create your views here.

class DoctorView(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class DoctorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        doctor = self.get_object
        self.perform_destroy(doctor)
        return Response({
            'message' : 'Doctor deleted successfully'
        }, status=status.HTTP_200_OK)