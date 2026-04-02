from django.urls import path
from django.contrib.auth.views import  LoginView, LogoutView
from .views import registration, dashboard

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registration/', registration, name='registration'),
    path('dashboard/', dashboard, name='dashboard')
]
