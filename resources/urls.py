from . import views
from django.urls import path

urlpatterns = [
    path('', views.ResourcesPage.as_view(), name='resources'),
    path('<int:resource_id>/', views.ResourceDetails.as_view(), name='resource_details'),
    path('favourite/<int:resource_id>/', views.FavouriteResource.as_view(), name='favourite_resource')
]
