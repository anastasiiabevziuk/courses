from django.db import models
from django.utils import timezone

class Cart(models.Model):
    title = models.CharField(max_length=255)
    price = models.FloatField()
    quantity = models.PositiveSmallIntegerField(default=0)
    session_key = models.CharField(max_length=32, null=True, blank=True)
    created_timestamp = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title



