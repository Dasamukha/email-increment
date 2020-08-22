from email_generator import views
from django.urls import path

urlpatterns = [
    path('', views.email),
    path('generated_email/', views.generated_email, name='generated'),
]
