from django import forms
from .models import Profile
from allauth.account.forms import SignupForm, LoginForm


# https://dev.to/danielfeldroy/customizing-django-allauth-signup-forms-2o1m
class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["username"].widget = forms.TextInput(
            attrs={"placeholder": "", "label": "", "class": "input-field py-1"}
        )
        self.fields["first_name"].widget = forms.TextInput(
            attrs={"placeholder": "", "label": "", "class": "input-field py-1"}
        )
        self.fields["last_name"].widget = forms.TextInput(
            attrs={"placeholder": "", "label": "", "class": "input-field py-1"}
        )
        self.fields["password1"].widget = forms.PasswordInput(
            attrs={"placeholder": "", "label": "", "class": "input-field py-1"}
        )
        self.fields["email"].widget = forms.EmailInput(
            attrs={"placeholder": "", "label": "", "class": "input-field py-1"}
        )
        self.fields["password2"].widget = forms.PasswordInput(
            attrs={"placeholder": "", "label": "", "class": "input-field py-1"}
        )

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        return user


class CustomLoginForm(LoginForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["login"].widget = forms.TextInput(
            attrs={"placeholder": "", "label": "", "class": "input-field py-1"}
        )
        self.fields["password"].widget = forms.PasswordInput(
            attrs={"placeholder": "", "label": "", "class": "input-field py-1"}
        )
    
        def login(self, *args, **kwargs):
            return super(MyCustomLoginForm, self).login(*args, **kwargs)

class GoalForm(forms.Form):
    goalName = forms.CharField(max_length=100, required=True, label='Goal Name')
