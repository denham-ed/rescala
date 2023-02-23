from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from allauth.account.forms import SignupForm


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Profile
        fields = "__all__"

class CustomSignupForm(SignupForm):
    class Mega:
        model = Profile
        fields = ['first_name', 'last_name']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["username"].label = ""
        self.fields["password1"].label = ""
        self.fields["password2"].label = ""

        self.fields['first_name'].required = True
        self.fields['last_name'].required = True

        self.fields["username"].widget = forms.TextInput(
            attrs={'placeholder': '',
                   'label': '',
                   'class': 'input-field py-1'})
        self.fields["password1"].widget = forms.PasswordInput(
            attrs={'placeholder': '',
                   'label': '',
                   'class': 'input-field py-1'})

        self.fields["password2"].widget = forms.PasswordInput(
            attrs={'placeholder': '',
                   'label': '',
                   'class': 'input-field py-1'})