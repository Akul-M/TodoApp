from django import forms
from .models import Task

class updateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['taskName', 'priority', 'date']
