from django.contrib import admin
from .models import Profile
from .forms import CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    model = Profile()
    add_form = CustomUserCreationForm()

admin.site.register(Profile, CustomUserAdmin)
