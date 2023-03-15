from django import forms
from .models import Profile
from allauth.account.forms import SignupForm, LoginForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Div
from crispy_forms.bootstrap import FormActions
from crispy_bootstrap5.bootstrap5 import FloatingField
from django.utils.safestring import mark_safe



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
        self.helper = FormHelper()
        self.helper.form_id = "id-custom-login-form"
        self.helper.form_method = "post"
 
        self.fields["login"].label = mark_safe('<i class="fa-solid fa-user-secret"></i> Username ')
        self.fields["password"].label = mark_safe('<i class="fa-solid fa-key"></i> Password ')
    

        self.helper.layout = Layout(
            Div(FloatingField("login")),
            Div(FloatingField("password")),
            Div(Submit(
                "submit","Log In", css_class="btn btn-md btn-light"
            ), css_class='d-flex justify-content-center')
        )

    
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

    #     self.fields["login"].widget = forms.TextInput(
    #         attrs={"placeholder": "", "label": "", "class": "input-field py-1"}
    #     )
    #     self.fields["password"].widget = forms.PasswordInput(
    #         attrs={"placeholder": "", "label": "", "class": "input-field py-1"}
    #     )
    
        def login(self, *args, **kwargs):
            return super(MyCustomLoginForm, self).login(*args, **kwargs)

class GoalForm(forms.Form):
    goalName = forms.CharField(max_length=100, required=True, label='Goal Name')
