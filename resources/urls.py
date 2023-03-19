from . import views
from django.urls import path

urlpatterns = [
    path('', views.LandingPage.as_view(), name='landing_page'),
    path('resources/', views.ResourcesPage.as_view(), name='resources'),
    path('resources/<int:resource_id>/', views.ResourceDetails.as_view(), name='resource_details')

]