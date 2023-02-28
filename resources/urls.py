from . import views
from django.urls import path

urlpatterns = [
    path('', views.LandingPage.as_view(), name='landing_page'),
    path('resources/', views.ResoucesPage.as_view(), name='resources'),
]