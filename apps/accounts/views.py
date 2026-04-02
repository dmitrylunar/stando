from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from apps.booking.models import Order
from django.contrib.auth.decorators import login_required
from datetime import datetime

# Create your views here.
def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

@login_required
def dashboard(request):
    active = Order.objects.filter(status__in=['new', 'confirmed'], user=request.user, datetime__gte=datetime.now())
    archive = Order.objects.filter(status__in=['done', 'cancelled'], user=request.user, datetime__lt=datetime.now())
    return render(request, 'accounts/dashboard.html', context={'archive': archive, 'active': active})