from .models import Session
from django import forms

class CreateSessionForm(forms.ModelForm):
    class Meta:
        model = Session
        fields = ['headline','date']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["headline"].widget = forms.TextInput(
            attrs={"placeholder": "", "label": "", "class": "input-field py-1"}
        )
# https://stackoverflow.com/questions/61076688/django-form-dateinput-with-widget-in-update-loosing-the-initial-value
        self.fields["date"].widget = forms.DateTimeInput(
             attrs={'class': 'form-control ps-5 input-field py-1', 'placeholder': '', 'type': 'date'}
        )
  