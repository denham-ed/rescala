from django.shortcuts import render
from allauth.account.views import SignupView
from .forms import CustomSignupForm


class CustomSignUpView(SignupView):
    template_name = "account/signup.html"

    form_class = CustomSignupForm

    # def get_context_data(self, **kwargs):
    #     context = super(self).get_context_data(**kwargs)
    #     signUpForm = CustomSignupForm(self.request.POST or None)
    #     context['form'] = signUpForm
    #     return context


    # if request.method == "POST":
    #     signup_form = CustomSignupForm(data=request.POST)
    #     # if signup_form.is_valid():
    #     #     print("WORKS!")
    #     # else:
    #     #     print("Nah")
    
    
