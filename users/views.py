from django.shortcuts import render
from allauth.account.views import SignupView
from .forms import CustomSignupForm


# class CustomSignUpView(SignupView):
#     template_name = "account/signup.html"
#     form_class = CustomSignupForm
    