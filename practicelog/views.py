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
            {   "testMessage": "Nothing to see yet",
                "create_session_form": CreateSessionForm()
            }
        )
    
    def post(self,request, *args, **kwargs):
        create_session_form = CreateSessionForm(data=request.POST)
        if create_session_form.is_valid():
            session = create_session_form.save(commit=False)
            session.user = request.user
            session.save()
            testMessage = "Good form work"
        else:
            testMessage = "Fucked it"
            
        return render(
            request, 'createlog.html',
            {   
                "testMessage": testMessage,
                "create_session_form": CreateSessionForm()
            }
        )

        