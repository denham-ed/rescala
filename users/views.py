from django.shortcuts import render
from allauth.account.views import SignupView
from .forms import CustomUserCreationForm


class CustomSignUpView(SignupView):
    template_name = "templates/account/signup.html"

    if request.method == "POST":
        signup_form = CustomUserCreationForm(data=request.POST)
        # if signup_form.is_valid():
        #     print("WORKS!")
        # else:
        #     print("Nah")
