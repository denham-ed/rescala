from django.shortcuts import render

# Create your views here.

class Dashboard(View):
    template_name = "dashboard.html"
    from django.views import View

    # @login_required
    def get(self, request):
        return render(
            request, 'dashboard.html',
            {"title": "Dashboard"}
        ) 