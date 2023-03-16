from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.views import View
from .forms import CreateSessionForm, EditSessionForm
from django.http import HttpResponseRedirect
from .models import Session
from users.forms import GoalForm
from datetime import datetime, timedelta, date
from wordcloud import WordCloud
import io
import base64
from django.contrib import messages
# Contenxt
from django.template import context



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
                messages.add_message(request, messages.SUCCESS, 'You have added a long term goal!')
                return HttpResponseRedirect(reverse('dashboard'))

    def update_goal(request, goal_id):
        if request.method == 'POST':
            current_user = request.user
            goal_complete = request.POST['goal-complete']
            current_user.goals[goal_id]['complete']=goal_complete
            current_user.save()
            messages.add_message(request, messages.SUCCESS, 'You have updated a long term goal.')
            return HttpResponseRedirect(reverse('dashboard'))


    def create_mood_cloud(self, sessions):
        aggregated_moods = []
        for session in sessions:
            aggregated_moods = aggregated_moods + session.moods
        mood_string = ' '.join(aggregated_moods)
        if not mood_string:
            return None
        # https://www.holisticseo.digital/python-seo/word-cloud/
        wordcloud = WordCloud(width = 1000, height = 700, mode="RGBA",background_color=None,color_func=lambda *args, **kwargs: (53, 88, 52)).generate(mood_string)
        image = wordcloud.to_image()
        buf = io.BytesIO()
        image.save(buf, format='png')
        # https://stackoverflow.com/questions/64974404/display-pil-image-object-in-django-template
        img_b64 = base64.b64encode(buf.getvalue()).decode('utf-8')
        return img_b64

    def create_calendar(self, sessions):
        start_date = date.today() - timedelta(days=29)
        dates = [start_date + timedelta(days=i) for i in range(30)]
        mapped_dates = [{'date': date, 'practice': False} for date in dates]
        for d in mapped_dates:
            # IS this right? looks like two loops!?
            for session in sessions:
                if any(session.date.strftime('%Y-%m-%d') == d['date'].strftime('%Y-%m-%d') for session in sessions):
                    d['practice'] = True
        return mapped_dates

    def aggregate_focus(self,sessions):
        focus_list = []
        for session in sessions:
            focus_list = focus_list + session.focus
        
        aggregated_focus = {}
        for focus in focus_list:
            if focus not in aggregated_focus:
                aggregated_focus[focus] = 1
            else:
                aggregated_focus[focus] += 1

        aggregated_as_list = [{"focus":x, "count":y} for x,y in aggregated_focus.items()]
        return aggregated_as_list

    def get_mins_practiced(self, sessions):
        start_date = date.today()
        # Weekly Minutes
        weekly_dates = [start_date - timedelta(days=i) for i in range(6)]
        weekly_minutes = sum(session.duration for session in sessions if session.date in weekly_dates)
        # Monthly Minutes
        monthly_dates = [start_date - timedelta(days=i) for i in range(30)]
        monthly_minutes = sum(session.duration for session in sessions if session.date in monthly_dates)
        # Total Minutes
        total_minutes = sum(session.duration for session in sessions)
        return { "weekly": weekly_minutes, "monthly": monthly_minutes, "total": total_minutes}

    def get(self, request):
        sessions = Session.objects.filter(user=request.user).order_by('-date')
        user = request.user
        
        return render(
                request, 'dashboard.html',
                {
                    "sessions": sessions,
                    "recent_sessions": sessions[:10],
                    "goalform": GoalForm(),
                    "goals": request.user.goals,
                    "dates": self.create_calendar(sessions),
                    "wordcloud": self.create_mood_cloud(sessions),
                    "practice_totals": self.get_mins_practiced(sessions),
                    "focus_list": self.aggregate_focus(sessions),
                    "user": user
                }
            ) 


class CreateLog(View):
    template_name = "createlog.html"

    def get(self, request):
        # user = request.user
        context={
            "form": CreateSessionForm(),
        }
        return render(
            request, 'createlog.html',context=context
        )

    def post(self, request, *args, **kwargs):
        create_session_form = CreateSessionForm(data=request.POST)
        if create_session_form.is_valid():
            user = request.user
            session = create_session_form.save(commit=False)
            session.user = request.user
            session.save()
            messages.add_message(request, messages.SUCCESS, 'Your practice has been logged successfully.')

            return HttpResponseRedirect(reverse('dashboard'))
        else:
            print(create_session_form.errors)
            context={"form": create_session_form}
            return render(
                request,
                'createlog.html',
                context=context
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
        messages.add_message(request, messages.SUCCESS, 'Your practice session has been deleted.')
        return HttpResponseRedirect(reverse('dashboard'))


class EditLog(View):
    template_name = "editlog.html"

    def get(self, request, session_id):
        session = get_object_or_404(Session, id=session_id)
        user = request.user
        initial_values = {
            'headline':session.headline,
            'date':session.date.strftime("%Y-%m-%d"),
            'duration':session.duration,
            'focus': session.focus,
            'summary':session.summary,
            'moods':session.moods
        }
        return render(
            request, 'editlog.html',
            {
                "form": EditSessionForm(session=session, initial=initial_values),
                "user": user,
                "session":session
            }
        )

    def post(self, request, *args, **kwargs):
        session_id = kwargs.get('session_id')
        session = Session.objects.get(id=session_id)
        form = EditSessionForm(session=session, data=request.POST)
        if form.is_valid():
            session.headline = form.cleaned_data['headline']
            session.date = form.cleaned_data['date']
            session.focus = form.cleaned_data['focus']
            session.duration = form.cleaned_data['duration']
            session.summary = form.cleaned_data['summary']
            session.moods = form.cleaned_data['moods']
            session.save()
            messages.add_message(request, messages.SUCCESS, 'You have successfully updated your practice session.')
            return redirect(f"/practice/{session_id}")
        else:
            return render(
                request,
                'editlog.html',
                {"form": form}
            )
