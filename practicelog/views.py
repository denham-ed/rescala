from django.shortcuts import render, reverse, get_object_or_404
from django.views import View
from .forms import CreateSessionForm
from django.http import HttpResponseRedirect
from .models import Session


class Dashboard(View):
    template_name = "dashboard.html"

    def get(self, request):
        sessions = get_object_or_404(Session)
        return render(
                request, 'dashboard.html',
                {
                    "sessions": session
                }
            ) 


class CreateLog(View):
    template_name = "createlog.html"

    def get(self, request):
        return render(
            request, 'createlog.html',
            { 
                "create_session_form": CreateSessionForm()
            }
        )

    def post(self, request, *args, **kwargs):
        create_session_form = CreateSessionForm(data=request.POST)
        if create_session_form.is_valid():
            session = create_session_form.save(commit=False)
            session.user = request.user
            session.save()
            return HttpResponseRedirect(reverse('dashboard'))
        else:
            return render(
                request,
                'createlog.html',
                {"create_session_form": CreateSessionForm()}
            )

