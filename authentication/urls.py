from django.urls import path
from .views import RegisterView, loginView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', loginView, name='login'),
]
