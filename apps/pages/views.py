from django.shortcuts import render
from apps.booking.models import Service

# Create your views here.
def home(request):
    return render(request, 'pages/home.html')

def service(request):
    service = Service.objects.all()
    return render(request, 'pages/service.html', context={'service': service})

def portfolio(request):
    return render(request, 'pages/portfolio.html')