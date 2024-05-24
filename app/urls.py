from django.urls import path
from . import views


urlpatterns = [
    path('', views.wpisy_przeglądów, name='wpisy_przeglądów'),
]
