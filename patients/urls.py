from django.urls import path
from .views import PatientView, PatientDetailView

urlpatterns = [
    path('', PatientView.as_view(), name='patients'),
    path('<int:pk>/', PatientDetailView.as_view(), name='patient_detail'),
]
