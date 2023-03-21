from . import views
from django.urls import path

urlpatterns = [
    path('resources/', views.ResourcesPage.as_view(), name='resources'),
    path('resources/<int:resource_id>/', views.ResourceDetails.as_view(), name='resource_details'),
    path('resources/favourite/<int:resource_id>/', views.FavouriteResource.as_view(), name='favourite_resource')

]