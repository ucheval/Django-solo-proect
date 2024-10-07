# Create your views here.
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def freelance_registration(request):
    return render(request, 'freelance-registration.html')

def freelance_login(request):
    return render(request, 'freelance-login.html')

def freelancedashboard(request):
    return render(request, 'freelancedashboard.html')

# Define other views similarly
