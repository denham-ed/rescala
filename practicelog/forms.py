from .models import Session
from django import forms

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
        super().__init__(*args, **kwargs)

        self.fields["headline"].widget = forms.TextInput(
            attrs={"placeholder": "", "label": "", "class": "input-field py-1"}
        )
# https://stackoverflow.com/questions/61076688/django-form-dateinput-with-widget-in-update-loosing-the-initial-value
        self.fields["date"].widget = forms.DateTimeInput(
             attrs={'class': 'form-control ps-5 input-field py-1', 'placeholder': '', 'type': 'date'}
        )

        self.fields["duration"].widget = forms.NumberInput(
            attrs={"placeholder": "", "label": "", "class": "form-control input-field py-1", 'type':'number'}
        )


        self.fields['focus'] = forms.MultipleChoiceField(choices=FOCUS_CHOICES, widget=forms.CheckboxSelectMultiple())
        # self.fields["focus"].widget = forms.CheckboxSelectMultiple(
        #     attrs={"placeholder": "", "label": "", "class": "form-control input-field py-1"}
        # )


  