from django.urls import path, include
from .views import LandingPage

urlpatterns = [
        path('', LandingPage.as_view(), name='landing_page'),
]
