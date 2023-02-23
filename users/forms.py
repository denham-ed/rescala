from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Profile
        fields = "__all__"