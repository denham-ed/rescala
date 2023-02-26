from django.urls import path, include
from .views import CustomSignUpView

urlpatterns = [
    path(
        'accounts/signup2/',
        CustomSignUpView.as_view(),
        name='custom_signup')
]