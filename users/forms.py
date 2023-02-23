from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from allauth.account.forms import SignupForm


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Profile
        fields = "__all__"

class CustomSignupForm(SignupForm):
    # class Meta:
    #     model = Profile
    #     fields = ['goals']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["username"].label = "Username"
        self.fields["password1"].label = "Password 1"
        self.fields["password2"].label = "Password 2"



        # self.fields["goals"].widget = forms.TextInput(
        #     attrs={'placeholder': '',
        #            'label': '',
        #            'class': 'input-field py-1'})

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

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        return user