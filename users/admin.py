from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Profile
from .forms import CustomSignupForm


# Credit: https://tinyurl.com/ykxsa4pw
class CustomUserAdmin(UserAdmin):
    """
    Adds Goals and Resources to User in
    to Django Admin panel
    """
    model = Profile()
    add_form = CustomSignupForm
    fieldsets = (
        *UserAdmin.fieldsets,
        ("Goals", {"fields": ("goals",)}),
        ("Resources", {"fields": ("resources",)}),
    )


admin.site.register(Profile, CustomUserAdmin)
