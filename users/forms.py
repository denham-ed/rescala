from django import forms
# from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from allauth.account.forms import SignupForm

# https://dev.to/danielfeldroy/customizing-django-allauth-signup-forms-2o1m

class CustomSignupForm(SignupForm):
    # class Meta:
    #     model = Profile
    #     fields = ('first_name','goals')

    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        

        # self.fields["username"].label = "Username"
        # self.fields["password1"].label = "Password 1"
        # self.fields["password2"].label = "Password 2"
        #         self.fields["em"].label = "Password 2"

        self.fields["username"].widget = forms.TextInput(
            attrs={'placeholder': '',
                   'label': '',
                   'class': 'input-field py-1'})
        self.fields["first_name"].widget = forms.TextInput(
            attrs={'placeholder': '',
                   'label': '',
                   'class': 'input-field py-1'})
        self.fields["last_name"].widget = forms.TextInput(
            attrs={'placeholder': '',
                   'label': '',
                   'class': 'input-field py-1'})
        self.fields["password1"].widget = forms.PasswordInput(
            attrs={'placeholder': '',
                   'label': '',
                   'class': 'input-field py-1'})

        self.fields["email"].widget = forms.EmailInput(
            attrs={'placeholder': '',
                   'label': '',
                   'class': 'input-field py-1'})

        self.fields["password2"].widget = forms.PasswordInput(
            attrs={'placeholder': '',
                   'label': '',
                   'class': 'input-field py-1'})

    def custom_signup(self, request, user):
        # Set the user's type from the form reponse
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        return user
