from django.db import models
from django.conf import settings

# Create your models here.


class Task(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    # Otros campos como fecha, estado de completado, etc.

    def __str__(self):
        return self.title
