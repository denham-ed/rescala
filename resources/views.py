from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.

class LandingPage(TemplateView):
    template_name = 'landing.html'

class ResoucesPage(TemplateView):
    template_name = 'resources.html'