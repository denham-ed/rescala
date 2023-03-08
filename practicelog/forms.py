from .models import Session
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from users.models import Profile
from django import forms
from datetime import datetime
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Div, Fieldset

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
    class Meta:
        model = Session
        fields = ["headline", "date", "duration", "focus", "summary", "moods"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "id-create-log-form"
        # self.helper.form_class = 'blueForms'
        self.helper.form_method = "post"
        self.helper.form_action = reverse_lazy("create_log")
        self.helper.layout = Layout(
            Div(
                Div(
                    "headline",
                    Div("date", "duration", css_class="d-flex justify-content-between"),
                    "focus",
                    css_class="col-md-4",
                ),
                Div("summary", css_class="col-md-4"),
                Div(Div("moods", css_class="two-col"), css_class="col-md-4"),
                css_class="row",
            )
        )

        self.helper.add_input(Submit("submit", "Submit"))

        self.fields["headline"].label = "Add a headline"
        self.fields["headline"].widget = forms.TextInput(
            attrs={
                "placeholder": "One sentence that describes your practice...",
            }
        )

        self.fields["date"].widget = forms.DateTimeInput(
            attrs={
                "type": "date",
                "max": datetime.now().date(),
            }
        )
        self.fields["duration"].label = "Duration (mins)"
        self.fields["duration"].widget = forms.NumberInput(
            attrs={"type": "number", "min": 1, "max": 720}
        )

        self.fields["focus"] = forms.MultipleChoiceField(
            label="Today I foccussed on:",
            choices=FOCUS_CHOICES,
            widget=forms.CheckboxSelectMultiple(),
            required=False,
        )

        self.fields["moods"] = forms.MultipleChoiceField(
            label="Today I felt:",
            choices=MOOD_CHOICES,
            widget=forms.CheckboxSelectMultiple(),
            required=False,
        )
        self.fields["summary"].label = "Reflections:"
        self.fields["summary"].widget = forms.Textarea(
            attrs={
                "placeholder": "Reflect on your practice. What went well? What will you work on next time?"
            }
        )
