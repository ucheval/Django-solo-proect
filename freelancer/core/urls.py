from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.freelance_registration, name='freelance_registration'),
    path('login/', views.freelance_login, name='freelance_login'),
    path('dashboard/', views.freelancedashboard, name='freelancedashboard'),
    # Add other paths similarly
]
