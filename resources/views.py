from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views.generic import ListView, TemplateView, View
from django.core.paginator import Paginator
from django.contrib import messages
from .models import Resource


class ResourcesPage(View):
    """
    A class-based view that represents the listing
    page for the Resources.
    The Resource shows a grid of available resources.
    Resources are paginated so 6 display on each page.
    """
    def get(self, request):
        """
        Handles the GET request for the Resources listing.
        Published (ie. not draft) resources are retrieved from
        the database and rendered, 6 to a page.
        """
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
    """
    A class-based view that represents a single Resource.
    The Resource (with headline, content and image) are rendered
    to the user.
    """
    def get(self, request, resource_id):
        """
        Handles the GET request for the Resource Detail view.
        The Resource is retrieved by ID from the database. Three
        other resources are provided (headline and image) for
        futher reading.

        If authenticated users have favourited the Resource, a solid star
        will be shown on the Resource image.

        Renders the resourcedetails template
        """
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
        """
        Handles the POST request for the Favourite Resource view.
        The user is identified from the request.
        If the Resource exists in the users Resources list,
        the Resource is removed.
        If the Resource does not exist in the users Resources list,
        the Resource is added.

        The Resource Details page is re-rendered and a confirmation
        message is displayed.
        """
        user = request.user
        resource = get_object_or_404(Resource, id=resource_id)
        if user.resources.filter(id=resource_id).exists():
            user.resources.remove(resource_id)
            messages.add_message(
                request,
                messages.SUCCESS,
                'This article has been removed from your favourites.')
        else:
            user.resources.add(resource)
            messages.add_message(
                request,
                messages.SUCCESS,
                'This article has been added to your favourites!')
        return redirect(reverse('resource_details', args=[resource_id]))
