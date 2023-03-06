from . import views
from django.urls import path

urlpatterns = [
    path('', views.Dashboard.as_view(), name='dashboard'),
    path('create', views.CreateLog.as_view(), name='create_log'),
    path('<int:session_id>/', views.SessionDetails.as_view(), name='session_details'),
    path('<int:session_id>/edit', views.EditLog.as_view(), name='edit_session'),
    path('<int:session_id>/delete', views.SessionDetails.delete_session, name='delete_session'),
    path('add-goal', views.Dashboard.add_goal, name='add_goal')
]