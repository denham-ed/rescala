from . import views
from django.urls import path

urlpatterns = [
    path('', views.Dashboard.as_view(), name='dashboard'),
    path('create', views.CreateLog.as_view(), name='create_log'),
    # path('resources', views.Resources.as_view(), name='resources'),
    # path('log-practice', views.Log_Practice.as_view(), name='log_practice'),
]