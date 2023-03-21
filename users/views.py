from django.shortcuts import render, redirect
from django.views.generic import View


class LandingPage(View):
    def get(self,request):
        if request.user.is_authenticated:
            return redirect('dashboard')
        return render(request, 'landing.html')
