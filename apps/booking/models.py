from django.db import models

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

class Order(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    service = models.CharField(max_length=20, choices=SERVICE_CHOISES, default='rec')
    datetime = models.DateTimeField()
    comment = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    created_at = models.DateTimeField(auto_now_add=True)