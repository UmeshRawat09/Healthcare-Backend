from django.urls import path
from .views import DoctorView, DoctorDetailView

urlpatterns = [
    path('', DoctorView.as_view(), name='doctors'),
    path('<int:pk>/', DoctorDetailView.as_view(), name='doctor_detail'),
]
