from django.shortcuts import render, redirect
from django.views.generic import View


class LandingPage(View):
    """
    A class-based view that represents the Landing page
    The landing page invites visitors to register or sign in
    """

    def get(self, request):
        """
        Handles the GET rquest for the landing page
        If the user is authenticated, they are redirected
        to the dashboard.
        If not, the 'landing' template renders.
        """
        if request.user.is_authenticated:
            return redirect('dashboard')
        return render(request, 'landing.html')
