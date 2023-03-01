from .models import Session
from django import forms

class CreateSessionForm(forms.ModelForm):
    class Meta:
        model = Session
        fields = ['date', 'duration', 'headline']