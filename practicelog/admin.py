from django.contrib import admin
from .models import Session


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    """
    Adds date, duration, headline and summary
    to Django Admin panel
    """
    list_display = ('date', 'duration', 'headline', 'summary')
