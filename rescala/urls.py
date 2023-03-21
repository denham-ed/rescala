from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('users.urls'), name='user_urls'),
    path('resources', include('resources.urls'), name='resources_urls'),
    path('practice/', include('practicelog.urls'), name='practice_urls'),
    path('summernote/', include('django_summernote.urls'))
]