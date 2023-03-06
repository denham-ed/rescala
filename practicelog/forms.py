from .models import Session
from django.contrib.auth.models import User
from users.models import Profile
from django import forms
from datetime import datetime
FOCUS_CHOICES = [
    ('listening', 'Listening'),
    ('scales', 'Scales and Arpeggios'),
    ('technique', 'Technique'),
    ('sightreading', 'Sightreading'),
    ('rhythm', 'Rhythm'),
    ('memorising', 'Memorising'),
    ('performing', 'Performing'),
    ('musicality', 'Musicality'),
]

class CreateSessionForm(forms.ModelForm):

    # focus = forms.MultipleChoiceField()

    class Meta:
        model = Session
        fields = ['headline', 'date', 'duration','focus','summary']



    def __init__(self, *args, **kwargs):
        # user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)


        self.fields["headline"].widget = forms.TextInput(
            attrs={"placeholder": "One sentence that describes your practice...", "label": "Add a headline", "class": "input-field py-1"}
        )
# https://stackoverflow.com/questions/61076688/django-form-dateinput-with-widget-in-update-loosing-the-initial-value
        self.fields["date"].widget = forms.DateTimeInput(
             attrs={'class': 'form-control input-field py-1', 'placeholder': '', 'type': 'date', 'max':datetime.now().date()}
        )

        self.fields["duration"].widget = forms.NumberInput(
            attrs={"placeholder": "", "label": "", "class": "form-control input-field py-1", 'type':'number'}
        )

        self.fields['focus'] = forms.MultipleChoiceField(choices=FOCUS_CHOICES, widget=forms.CheckboxSelectMultiple(), required=False )
        self.fields['summary'].widget=forms.Textarea(attrs={"placeholder":"Reflect on your practice. What went well? What will you work on next time?"})



  