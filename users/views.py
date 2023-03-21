from django.shortcuts import render
from django.views.generic import View


class LandingPage(View):
    def get(self,request):
        return render(request, 'landing.html')
