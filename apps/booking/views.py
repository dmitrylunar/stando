from django.shortcuts import render, redirect
from .forms import OrderForm

# Create your views here.
def booking(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking')
    else:
        form = OrderForm()
    return render(request, 'booking/booking.html', {'form': form})
