from django.contrib import admin
from .models import Resource

# Register your models here.
@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'status')
    prepopulated_fields = {'slug': ('title',)}