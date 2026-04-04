from django.db import models
from django.conf import settings

# Create your models here.
class UserProfile(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    discount = models.FloatField(default=0)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

