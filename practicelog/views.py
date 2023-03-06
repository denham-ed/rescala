from django.shortcuts import render, reverse, get_object_or_404
from django.views import View
from .forms import CreateSessionForm
from django.http import HttpResponseRedirect
from .models import Session
from users.forms import GoalForm


# Dashboard
class Dashboard(View):
    template_name = "dashboard.html"

    def add_goal(request):
        if request.method == 'POST':
            current_user = request.user
            form = GoalForm(request.POST)
            if form.is_valid():
                goal = form.cleaned_data['goalName']
                current_user.goals.append({
                    'goal': goal,
                    'complete':0
                })
                current_user.save()
                print(goal)
                # Sessions
                sessions = Session.objects.filter(user=request.user).order_by('-date')
                recent_sessions = sessions[:10]
                return HttpResponseRedirect(reverse('dashboard'))

    def get(self, request):
        sessions = Session.objects.filter(user=request.user).order_by('-date')
        recent_sessions = sessions[:10]
        return render(
                request, 'dashboard.html',
                {
                    "sessions": sessions,
                    "recent_sessions": recent_sessions,
                    "goalform": GoalForm(),
                    "goals":request.user.goals
                }
            ) 


class CreateLog(View):
    template_name = "createlog.html"

    def get(self, request):
        user = request.user
        return render(
            request, 'createlog.html',
            { 
                "create_session_form": CreateSessionForm(),
                "user":user
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


class SessionDetails(View):
    template_name = 'sessiondetails.html'

    def get(self, request, session_id, *args, **kwargs):
        session = get_object_or_404(Session, id=session_id)

        return render(
            request, 'sessiondetails.html',
            {
                "session": session
            }
        )
    
    def delete_session(request, session_id):
        session = get_object_or_404(Session, id=session_id)
        session.delete()
        return HttpResponseRedirect(reverse('dashboard'))


