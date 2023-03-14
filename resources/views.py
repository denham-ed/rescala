from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Resource

# Create your views here.

class LandingPage(TemplateView):
    template_name = 'landing.html'

class ResourcesPage(TemplateView):
    # template_name = 'resources.html'

    def get(self,request):
        resources = Resource.objects.all()

        return render(
            request, 'resources.html',{
                "resources": resources
            }
        )