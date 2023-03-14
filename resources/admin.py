from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Resource

# Register your models here.
@admin.register(Resource)
class ResourceAdmin(SummernoteModelAdmin):
    list_display = ('title', 'content', 'status')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields =('content')