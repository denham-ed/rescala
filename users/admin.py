from django.contrib import admin
from .models import Profile
from .forms import CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin

# https://www.youtube.com/watch?v=1BeZxMbSZNI
class CustomUserAdmin(UserAdmin):
    model = Profile()
    add_form = CustomUserCreationForm
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Goals',{
            'fields':(
                'goals',
            )
            }
        ),         (
            'Resources',{
            'fields':(
                'resources',
            )
            }
        )
        
    )

admin.site.register(Profile, CustomUserAdmin)
