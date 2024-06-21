# todo/forms.py
from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    due_date = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={"type": "datetime-local"}), required=False
    )
    edit_reason = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = Task
        fields = ["title", "description", "due_date", "edit_reason"]
