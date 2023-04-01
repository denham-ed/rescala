from django import forms
from .models import Profile
from allauth.account.forms import SignupForm, LoginForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Div
from crispy_forms.bootstrap import FormActions
from crispy_bootstrap5.bootstrap5 import FloatingField
from django.utils.safestring import mark_safe
from django.shortcuts import reverse


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(
        max_length=30,
        label=mark_safe('<i class="fa-solid fa-user"></i> First Name '),
            error_messages={'required': 'A first name is required'},
        )
    last_name = forms.CharField(
        max_length=30,
        label=mark_safe('<i class="fa-solid fa-user"></i> Last Name '),
            error_messages={'required': 'A last name is required'},
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "id-custom-signup-form"
        self.helper.form_method = "post"
        self.helper.attrs = {"novalidate": ''}
        self.helper.layout = Layout(
            Div(FloatingField("username")), 
            Div(FloatingField("first_name")),
            Div(FloatingField("last_name")),
            Div(FloatingField("password1")),
            Div(FloatingField("password2")),
            Div(Submit(
                "submit","Register", css_class="btn btn-md btn-light"
            ), css_class='d-flex justify-content-center')
        )
        self.fields["username"] = forms.CharField(
            label=mark_safe('<i class="fa-solid fa-user-secret"></i> Enter A Username '),
            error_messages={'required': 'You must select a username for Rescala'},
            widget=forms.TextInput(),
        )
        self.fields["password1"].label=mark_safe('<i class="fa-solid fa-key"></i> Enter A Password ')
        self.fields["password1"].error_messages={'required': 'You must enter a password'}
        self.fields["password2"].label=mark_safe('<i class="fa-solid fa-lock"></i> Re-Enter Your Password ')
        self.fields["password2"].error_messages={'required': 'Please confirm your password'}

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        return user


class CustomLoginForm(LoginForm):
    error_messages = {
        "username_password_mismatch": (
            "Sorry! Your username or password isn't quite right. Please try again."
        ),
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "id-custom-login-form"
        self.helper.form_method = "post"
        self.helper.attrs = {"novalidate": ''}
        self.fields["login"] = forms.CharField(
                label=mark_safe('<i class="fa-solid fa-user-secret"></i> Username '),
                error_messages={'required': 'Please enter your Rescala username'}
        )
        self.fields["password"].label=mark_safe('<i class="fa-solid fa-key"></i> Password ')
        self.fields["password"].error_messages={'required': 'Please enter your password'}

        self.helper.layout = Layout(
            Div(FloatingField("login")),
            Div(FloatingField("password")),
            Div("remember", css_class='light-text'),
            Div(Submit(
                "submit","Sign In", css_class="btn btn-md btn-light"
            ), css_class='d-flex justify-content-center')
        )

        def login(self, *args, **kwargs):
            return super(MyCustomLoginForm, self).login(*args, **kwargs)

class GoalForm(forms.Form):

    goal_name = forms.CharField(max_length=100, required=True, label='Set a Long Term Goal')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "id-add-goal-form"
        self.helper.form_method = "post"
        self.helper.form_action = reverse("add_goal")
        self.helper.attrs = {"novalidate": ''}
        self.helper.layout = Layout(
            Div(FloatingField("goal_name")), 
            Div(Submit(
                "submit","Add Goal", css_class="btn btn-md btn-dark"
            ), css_class='d-flex justify-content-center')
        )
        self.fields["goal_name"].error_messages = {
            'required':'You must enter a goal'
        }
