from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views.generic import ListView, TemplateView, View
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect

from .models import Resource

class LandingPage(TemplateView):
    template_name = 'landing.html'

class ResourcesPage(View):

    # Cloudinary Docs ????
    def image_effects(request):
        return dict(
            IMAGE_EFFECTS = dict(
                format = "png",
                transformation = [
                    dict(height=95, width=95, crop="thumb", gravity="face", radius=20)
                ]
            )
        )

    def get(self, request):
        # resources = Resource.objects.all()
        resources = Resource.objects.filter(status=1)
        paginator = Paginator(resources, 6)

        page_number = request.GET.get('page')
        paginated_resources = paginator.get_page(page_number)

        image_effects = self.image_effects()

        return render(
            request, 'resources.html',{
                "resources": paginated_resources,
                "IMAGE_EFFECTS": image_effects
            }
        )

class ResourceDetails(View):

    def get(self,request, resource_id):

        resource = get_object_or_404(Resource, id=resource_id)
        articles = Resource.objects.exclude(id=resource_id).filter(status=1)
        return render(
            request, 'resourcedetails.html', {
                "resource": resource,
                "articles": articles[:3]
            }
        )


class FavouriteResource(View):
    def post(self, request, resource_id):
        user = request.user
        resource = get_object_or_404(Resource, id=resource_id)
        if user.resources.filter(id=resource_id).exists():
            user.resources.remove(resource_id)
        else:
            user.resources.add(resource)
        return redirect(reverse('resource_details', args=[resource_id]))

