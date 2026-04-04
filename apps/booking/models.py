from django.db import models
from django.conf import settings

SERVICE_CHOISES = [
    ('rec', 'Запись'),
    ('master', 'Сведение'),
    ('instrumental', 'Аранжировка'),
    ('lyrics', 'Текст')
]

STATUS_CHOICES = [
    ('new', 'Новый'),
    ('confirmed', 'Подтвержден'),
    ('done', 'Выполнен'),
    ('cancelled', 'Отменен')
]

class Service(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True)
    datetime = models.DateTimeField()
    comment = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    created_at = models.DateTimeField(auto_now_add=True)