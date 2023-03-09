from django.shortcuts import render, reverse, get_object_or_404
from django.views import View
from .forms import CreateSessionForm, EditSessionForm
from django.http import HttpResponseRedirect, HttpResponse
from .models import Session
from users.forms import GoalForm
from allauth.exceptions import ImmediateHttpResponse
from datetime import datetime, timedelta, date

# Word Cloud
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd
from typing import Any, Optional
import io
import base64









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
        # Sesssions
        sessions = Session.objects.filter(user=request.user).order_by('-date')
        recent_sessions = sessions[:10]
        # Calendar
        start_date = date.today() - timedelta(days=29)
        dates = [start_date + timedelta(days=i) for i in range(30)]
        mapped_dates = [{'date': date, 'practice': False, 'headline': None} for date in dates]
        for d in mapped_dates:
            for session in sessions:
                if any(session.date.strftime('%Y-%m-%d') == d['date'].strftime('%Y-%m-%d') for session in sessions):
                    d['practice'] = True

        # Moods
        aggregated_moods = []
        for session in sessions:
            aggregated_moods = aggregated_moods + session.moods
            
        mood_string = ' '.join(aggregated_moods)
        wordcloud = WordCloud(width = 1000, height = 700).generate(mood_string)

        image = wordcloud.to_image()
        buf = io.BytesIO()
        image.save(buf, format='png')

        # Encode buffer contents as base64
        img_b64 = base64.b64encode(buf.getvalue()).decode('utf-8')

        # return HttpResponse(buffer.getvalue(), content_type='image/png')
        return render(
                request, 'dashboard.html',
                {
                    "sessions": sessions,
                    "recent_sessions": recent_sessions,
                    "goalform": GoalForm(),
                    "goals":request.user.goals,
                    "dates": mapped_dates,
                    "moods":aggregated_moods,
                    "wordcloud":img_b64,
                    "image":image
                }
            ) 


class CreateLog(View):
    template_name = "createlog.html"

    def get(self, request):
        user = request.user
        return render(
            request, 'createlog.html',
            {
                "form": CreateSessionForm(),
                "user": user
            }
        )

    def post(self, request, *args, **kwargs):
        create_session_form = CreateSessionForm(data=request.POST)
        if create_session_form.is_valid():
            # Capture Goal Inputs
            user = request.user
            # goals = [request.POST.get(f'goal-{i}') for i in range(1, 100) if request.POST.get(f'goal-{i}')]
            # user.goals = [{"goal": user.goals[i]['goal'], "complete": goal} for i, goal in enumerate(goals)]
            session = create_session_form.save(commit=False)
            session.user = request.user
            session.save()
            user.save()
            return HttpResponseRedirect(reverse('dashboard'))
        else:
            return render(
                request,
                'createlog.html',
                {"form": CreateSessionForm()}
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
            session.save()
            return HttpResponseRedirect(reverse('dashboard'))
        else:
            return render(
                request,
                'editlog.html',
                {"form": EditSessionForm()}
            )
