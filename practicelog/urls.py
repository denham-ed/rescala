from . import views
from django.urls import path

urlpatterns = [
    path('', views.Dashboard.as_view(), name='dashboard'),
    path('create', views.CreateLog.as_view(), name='create_log'),
    path('<int:session_id>/', views.SessionDetails.as_view(), name='session_details')
]