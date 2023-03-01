from django.shortcuts import render
from django.views import View
from .forms import CreateSessionForm

# Create your views here.

class Dashboard(View):
    template_name = "dashboard.html"
    from django.views import View

    def get(self, request):
        return render(
            request, 'dashboard.html'
        ) 


class CreateLog(View):
    template_name = "createlog.html"
    from django.views import View

    def get(self, request):
        return render(
            request, 'createlog.html',
            {
                "create_session_form": CreateSessionForm()
            }
        )
        