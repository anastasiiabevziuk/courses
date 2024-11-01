from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Cart(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=255)
    price = models.FloatField()
    quantity = models.PositiveSmallIntegerField(default=0)
    session_key = models.CharField(max_length=32, null=True, blank=True)
    created_timestamp = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title
