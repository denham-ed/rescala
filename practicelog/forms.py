from .models import Session
from django.contrib.auth.models import User
from users.models import Profile
from django import forms
from datetime import datetime

FOCUS_CHOICES = [
    ("listening", "Listening"),
    ("scales", "Scales and Arpeggios"),
    ("technique", "Technique"),
    ("sightreading", "Sightreading"),
    ("rhythm", "Rhythm"),
    ("memorising", "Memorising"),
    ("performing", "Performing"),
    ("musicality", "Musicality"),
]

MOOD_CHOICES = [
    ("confident", "Confident"),
    ("anxious", "Anxious"),
    ("hopeful", "Hopeful"),
    ("pessimistic", "Pessimistic"),
    ("motivated", "Motivated"),
    ("discouraged", "Discouraged"),
    ("determined", "Determined"),
    ("overwhelmed", "Overwhelmed"),
    ("ambitious", "Ambitious"),
    ("doubtful", "Doubtful"),
    ("focused", "Focused"),
    ("distracted", "Distracted"),
    ("excited", "Excited"),
    ("bored", "Bored"),
    ("engaged", "Engaged"),
    ("disinterested", "Disinterested"),
    ("inspired", "Inspired"),
    ("uninspired", "Uninspired"),
    ("enthusiastic", "Enthusiastic"),
    ("disheartened", "Disheartened"),
    ("empowered", "Empowered"),
    ("defeated", "Defeated"),
    ("encouraged", "Encouraged"),
    ("despondent", "Despondent"),
    ("curious", "Curious"),
    ("frustrated", "Frustrated"),
    ("accomplished", "Accomplished"),
    ("disappointed", "Disappointed"),
    ("productive", "Productive"),
    ("procrastinating", "Procrastinating"),
]


class CreateSessionForm(forms.ModelForm):

    # focus = forms.MultipleChoiceField()

    class Meta:
        model = Session
        fields = ["headline", "date", "duration", "focus", "summary", "moods"]

    def __init__(self, *args, **kwargs):
        # user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        self.fields["headline"].widget = forms.TextInput(
            attrs={
                "placeholder": "One sentence that describes your practice...",
                "label": "Add a headline",
                "class": "input-field py-1",
            }
        )
        # https://stackoverflow.com/questions/61076688/django-form-dateinput-with-widget-in-update-loosing-the-initial-value
        self.fields["date"].widget = forms.DateTimeInput(
            attrs={
                "class": "form-control input-field py-1",
                "placeholder": "",
                "type": "date",
                "max": datetime.now().date(),
            }
        )

        self.fields["duration"].widget = forms.NumberInput(
            attrs={
                "placeholder": "",
                "label": "",
                "class": "form-control input-field py-1",
                "type": "number",
            }
        )

        self.fields["focus"] = forms.MultipleChoiceField(
            choices=FOCUS_CHOICES, widget=forms.CheckboxSelectMultiple(), required=False
        )

        self.fields["moods"] = forms.MultipleChoiceField(
            choices=MOOD_CHOICES, widget=forms.CheckboxSelectMultiple(), required=False
        )

        self.fields["summary"].widget = forms.Textarea(
            attrs={
                "placeholder": "Reflect on your practice. What went well? What will you work on next time?"
            }
        )
        # CHAT GPT
    def moods_as_columns(self):
            """
            Render the moods field as two columns of checkboxes.
            """
            # Get the list of choices
            choices = self.fields['moods'].choices
            # Determine the number of choices per column
            num_choices = len(choices)
            num_per_column = num_choices // 2
            # Split the choices into two lists
            col1 = choices[:num_per_column]
            col2 = choices[num_per_column:]
            # Render each column as a string of HTML
            col1_html = ''.join('<label"><input class="mx-1" type="checkbox" name="%s" value="%s">%s</label><br>' % ('moods', choice[0], choice[1]) for choice in col1)
            col2_html = ''.join('<label><input class="mx-1" type="checkbox" name="%s" value="%s">%s</label><br>' % ('moods', choice[0], choice[1]) for choice in col2)
            # Combine the columns and wrap in a div
            return '<div class="row"><div class="col-sm-6">%s</div><div class="col-sm-6">%s</div></div>' % (col1_html, col2_html)
