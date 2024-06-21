from django.db import models
from django.conf import settings

# Create your models here.


class Task(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    due_date = models.DateTimeField(
        null=True, blank=True
    )  # nos permite asegurar que ciertas tareas se realizen en un momento espoecifico.
    edit_reason = models.TextField(
        null=True, blank=True
    )  # nos va a devolver una razon por la cual se edita la tarea.
    # Otros campos como fecha, estado de completado, etc.

    def __str__(self):
        return self.title


class TaskEditHistory(models.Model):
    """guarda el historial de ediciones, cuando una tarea es editad se puede crear una instancia de TaskEditHistory para registrar quien hizo la edición, cuando  se hizo y el motivo del cambio"""

    task = models.ForeignKey(
        Task, on_delete=models.CASCADE, related_name="edit_history"
    )
    edited_at = models.DateTimeField(auto_now_add=True)
    edit_reason = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"Edit by {self.user.username} on {self.edited_at}"
