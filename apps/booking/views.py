from django.shortcuts import render, redirect
from .forms import OrderForm

# Create your views here.
def booking(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            if request.user.is_authenticated:
                order.user = request.user
            else:
                order.user = None
            order.save()
            return redirect('success')
    else:
        form = OrderForm()
    return render(request, 'booking/booking.html', {'form': form})

def booking_success(request):
    return render(request, 'booking/booking_success.html')