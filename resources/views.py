from django.shortcuts import render
from django.views.generic import ListView, TemplateView, View
from django.core.paginator import Paginator
from .models import Resource

# Create your views here.

class LandingPage(TemplateView):
    template_name = 'landing.html'





class ResourcesPage(View):

    # Cloudinary Docs
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
        paginator = Paginator(resources, 3)

        page_number = request.GET.get('page')
        paginated_resources = paginator.get_page(page_number)

        image_effects = self.image_effects()

        return render(
            request, 'resources.html',{
                "resources": paginated_resources,
                "IMAGE_EFFECTS": image_effects
            }
        )