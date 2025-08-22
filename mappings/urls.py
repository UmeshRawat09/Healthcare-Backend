from django.urls import path
from .views import MappingView, PatientMapping, MappingDelete


urlpatterns = [
    path('', MappingView.as_view(), name='mapping'),
    path('<int:patient_id>/', PatientMapping.as_view(), name='patient_mapping'),
    path('<int:pk>/', MappingDelete.as_view, name='mapping_delete')
]
