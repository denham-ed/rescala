from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Resource

@admin.register(Resource)
class ResourceAdmin(SummernoteModelAdmin):
    list_display = ('title', 'excerpt', 'status')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields =('content')
    actions = ['publish_resource']

    def publish_resource(self, request, queryset):
        queryset.update(status=1)