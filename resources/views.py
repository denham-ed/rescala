from django.shortcuts import render
from django.views.generic import ListView, TemplateView, View
from django.core.paginator import Paginator
from .models import Resource

# Create your views here.

class LandingPage(TemplateView):
    template_name = 'landing.html'

class ResourcesPage(View):
    def get(self, request):

        resources = Resource.objects.all()
        paginator = Paginator(resources, 3)

        page_number = request.GET.get('page')
        paginated_resources = paginator.get_page(page_number)

        return render(
            request, 'resources.html',{
                "resources": paginated_resources
            }
        )