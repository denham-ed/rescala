from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Resource


@admin.register(Resource)
class ResourceAdmin(SummernoteModelAdmin):
    """
    Adds title, excerpt, and status
    to Django Admin panel.
    Users Django Summernote to add WYSIWYG 
    functionality to the content field.
    Creates Publish Resource as an admin
    action.
    """
    list_display = ('title', 'excerpt', 'status')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content')
    actions = ['publish_resource']

    def publish_resource(self, request, queryset):
        queryset.update(status=1)