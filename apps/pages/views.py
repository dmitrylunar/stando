from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'pages/home.html')

def service(request):
    return render(request, 'pages/service.html')

def portfolio(request):
    return render(request, 'pages/portfolio.html')