from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views.generic import ListView, TemplateView, View
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Resource


class ResourcesPage(View):
    def get(self, request):
        resources = Resource.objects.filter(status=1)
        paginator = Paginator(resources, 6)
        page_number = request.GET.get('page')
        paginated_resources = paginator.get_page(page_number)
        return render(
            request, 'resources.html', {
                "resources": paginated_resources
            }
        )


class ResourceDetails(View):
    def get(self, request, resource_id):
        resource = get_object_or_404(Resource, id=resource_id)
        user = request.user
        if user.is_authenticated:
            favourite = user.resources.filter(id=resource_id).exists()
        else:
            favourite = False     
        articles = Resource.objects.exclude(id=resource_id).filter(status=1)
        return render(
            request, 'resourcedetails.html', {
                "resource": resource,
                "articles": articles[:3],
                "favourite": favourite
            }
        )


class FavouriteResource(View):
    def post(self, request, resource_id):
        user = request.user
        resource = get_object_or_404(Resource, id=resource_id)
        if user.resources.filter(id=resource_id).exists():
            user.resources.remove(resource_id)
            messages.add_message(request, messages.SUCCESS, 'This article has been removed from your favourites.')
        else:
            user.resources.add(resource)
            messages.add_message(request, messages.SUCCESS, 'This article has been added to your favourites!')
        return redirect(reverse('resource_details', args=[resource_id]))
