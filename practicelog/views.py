import random
from datetime import datetime, timedelta, date
from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.contrib import messages
from django.template import context
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from users.forms import GoalForm
from .forms import CreateSessionForm, EditSessionForm
from .models import Session


class Dashboard(LoginRequiredMixin, View):
    """
    A class-based view that represents Dashboard for an authorised user.
    The dashboard displays a number of widgets including a calendar,
    a list of recent practice sessions, a graph of focus areas,
    and a word cloud representing the user's logged moods.
    """
    def add_goal(request):
        """
        Handles a submitted Add Goal form from the dashboard.
        If the form is valid, the goal is added to the user's Profile.
        The user is then redirected to the dashboard.
        A message confirms the added goal.
        """
        if request.method == 'POST':
            current_user = request.user
            form = GoalForm(request.POST)
            if form.is_valid():
                goal = form.cleaned_data['goal_name']
                current_user.goals.append({
                    'goal': goal,
                    'complete': 0
                })
                current_user.save()
                messages.add_message(
                    request,
                    messages.SUCCESS,
                    'You have added a long term goal!')
                return redirect(reverse('dashboard'))
            else:
                messages.add_message(
                    request,
                    messages.WARNING,
                    'Oops - you need to enter a goal. Please try again.')
                return redirect(reverse('dashboard'))

    def update_goal(request, goal_id):
        """
        Handles a submitted Update Goal request from the dashboard.
        The goal is identified by it's index in the User's goal list.
        The goal's 'complete' attribute is updated.
        The user is then redirected to the dashboard.
        A message confirms the updated goal.
        """
        if request.method == 'POST':
            print("POSTING")
            current_user = request.user
            goal_complete = request.POST['goal-complete']
            current_user.goals[goal_id]['complete'] = goal_complete
            current_user.save()
            messages.add_message(
                    request,
                    messages.SUCCESS,
                    'You have updated a long term goal.')
            return redirect('dashboard')

    def delete_goal(request, goal_id):
        """
        Handles a submitted Delete Goal request from the dashboard.
        The goal is identified by it's index in the User's goal list.
        The goal is removed from the user's goals list.
        The user is then redirected to the dashboard.
        A message confirms the delete goal.
        """
        if request.method == 'POST':
            current_user = request.user
            current_user.goals.remove(current_user.goals[goal_id])
            current_user.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'You have removed a long term goal.')
        return redirect('dashboard')

    def create_mood_cloud(self, sessions):
        """
        Aggregates the mood list from each logged session.
        Returns the aggregated list as a list of dictionaries
        with the mood and a count to represent how often they appear.
        This list is shuffled to create a random order.
        """
        aggregated_moods = []
        for session in sessions:
            aggregated_moods = aggregated_moods + session.moods
        mood_dict = {}
        for mood in aggregated_moods:
            if mood not in mood_dict:
                mood_dict[mood] = 1
            else:
                mood_dict[mood] += 1
        total_moods = sum(mood_dict.values())
        aggregated_as_list = [{"mood": x, "count": round(y/total_moods, 2)
                              * 100} for x, y in mood_dict.items()]
        random.shuffle(aggregated_as_list)
        return aggregated_as_list

    def create_calendar(self, sessions):
        """
        Prepares an list of dates for the calendar widget
        on the dashboard
        Creates a list of dates from the last 30 days.
        Loops through the list to identify dates where
        practice has been logged.
        Returns an list of dictionaries with a date and practice
        (boolean) attribute.
        """
        start_date = date.today() - timedelta(days=29)
        dates = [start_date + timedelta(days=i) for i in range(30)]
        mapped_dates = [{'date': date, 'practice': False} for date in dates]
        for d in mapped_dates:
            for session in sessions:
                if any(session.date.strftime('%Y-%m-%d') ==
                       d['date'].strftime('%Y-%m-%d') for session in sessions):
                    d['practice'] = True
        return mapped_dates

    def aggregate_focus(self, sessions):
        """
        Prepares a list of displaying a chart on the dashboard.
        Function takes a list of sessions and aggregates the recorded
        foci of each.
        Returns a lsit of dictionaries that contains the mood itself and a
        count to represent how often they appear in the sessions.
        """
        focus_list = []
        for session in sessions:
            focus_list = focus_list + session.focus
        aggregated_focus = {}
        for focus in focus_list:
            if focus not in aggregated_focus:
                aggregated_focus[focus] = 1
            else:
                aggregated_focus[focus] += 1
        aggregated_as_list = [{"focus": x, "count": y}
                              for x, y in aggregated_focus.items()]
        return aggregated_as_list

    def get_mins_practiced(self, sessions):
        """
        Prepares a dictionary for rendering the minutes practiced
        widget on the dashboard.
        Calculates the number of minutes of logged pracitce
        for the last 7 days, 30 days and all sessions.
        Returns a dictionary with these totals.
        """
        start_date = date.today()
        weekly_dates = [start_date - timedelta(days=i) for i in range(6)]
        weekly_minutes = sum(session.duration
                             for session in sessions
                             if session.date in weekly_dates)
        monthly_dates = [start_date - timedelta(days=i) for i in range(30)]
        monthly_minutes = sum(session.duration
                              for session in sessions
                              if session.date in monthly_dates)
        total_minutes = sum(session.duration for session in sessions)
        return {
            "weekly": weekly_minutes,
            "monthly": monthly_minutes,
            "total": total_minutes
        }

    def get(self, request):
        """
        Handles the GET request for the app's dashboard.
        Renders the 'dashboard' template with context for each widget.
        """
        sessions = Session.objects.filter(user=request.user).order_by('-date')
        user = request.user
        resources = user.resources.all()
        return render(
                request, 'dashboard.html',
                {
                    "sessions": sessions,
                    "recent_sessions": sessions[:5],
                    "goalform": GoalForm(),
                    "goals": request.user.goals,
                    "dates": self.create_calendar(sessions),
                    "wordcloud": self.create_mood_cloud(sessions),
                    "practice_totals": self.get_mins_practiced(sessions),
                    "focus_list": self.aggregate_focus(sessions),
                    "user": user,
                    "resources": resources
                }
            )


class CreateLog(LoginRequiredMixin, View):
    """
    A class-based view representing the Create Session Log view.
    It is viewable by authorized users.
    It renders an instance of the Create Session Form, allowing
    users to log a practice session.
    """
    def get(self, request):
        """
        Handles the GET request for the Create Session log view.
        Renders the 'createlog' template with an instance of the
        Create Sesion Form as context.
        """
        context = {
            "form": CreateSessionForm(),
        }
        return render(
            request, 'createlog.html', context=context
        )

    def post(self, request, *args, **kwargs):
        """
        Handles the submission of an instnace of the Create Session form.
        If the form is valid, a new session is created.
        The current user is attached to the session as a FK.
        The user is then redirected to the dashboard and a message
        confirming the successful creation is rendered.

        If invalid, the form is rerendered with errors.
        """
        create_session_form = CreateSessionForm(data=request.POST)
        if create_session_form.is_valid():
            user = request.user
            session = create_session_form.save(commit=False)
            session.user = request.user
            session.save()
            messages.add_message(
                    request,
                    messages.SUCCESS,
                    'Your practice has been logged successfully.')
            return redirect('dashboard')
        else:
            context = {"form": create_session_form}
            return render(
                request,
                'createlog.html',
                context=context
            )


class SessionDetails(LoginRequiredMixin, View):
    """
    A class-based view that represents a Read-Only view of the session's
    Details for an authorised user.
    The view displays the summary, duration, date, moods and foci of
    the session.
    The user can delete the session using a button.
    """
    def get(self, request, session_id, *args, **kwargs):
        """
        Handles the GET request for the Session Details view.
        Retrieves the session by it's ID from the database and provides
        it as context.
        Renders the 'sessiondetails' template.
        """
        session = get_object_or_404(Session, id=session_id)

        return render(
            request, 'sessiondetails.html',
            {
                "session": session
            }
        )

    def delete_session(request, session_id):
        """
        Handles a delete request by the user.
        The session is identified form the database by its ID.
        The session is then removed from the database.
        A message, confirming deletion, is rendered to the user
        after redirecting them to the dashboard.
        """
        session = get_object_or_404(Session, id=session_id)
        session.delete()
        messages.add_message(
                request,
                messages.SUCCESS,
                'Your practice session has been deleted.')
        return redirect('dashboard')


class EditLog(LoginRequiredMixin, View):
    """
    A class-based view representing the Edit Session view
    It is viewable by authorized users.
    It contains an instnace of the Edit Session form, allowing
    users to edit an existing session.
    """
    def get(self, request, session_id):
        """
        Handles the GET request for the Edit Session view.
        Retrieves the session by it's ID from the database and
        prepopulates an instance of the Edit Session form
        before rendering.
        Renders the 'editlog' template.
        """
        session = get_object_or_404(Session, id=session_id)
        user = request.user
        initial_values = {
            'headline': session.headline,
            'date': session.date.strftime("%Y-%m-%d"),
            'duration': session.duration,
            'focus': session.focus,
            'summary': session.summary,
            'moods': session.moods
        }
        return render(
            request, 'editlog.html',
            {
                "form": EditSessionForm(
                    session=session,
                    initial=initial_values),
                "user": user,
                "session": session
            }
        )

    def post(self, request, *args, **kwargs):
        """
        Handles the POST request for the Edit Session view.
        Retrieves the session by it's ID from the database.
        If the form is valid, the session will be updated with
        the new form data.
        The user is redirected to the session details page.
        A message is rendered confirming the update.

        If invalid, the form is rerendered with errors.
        """
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
            messages.add_message(
                    request,
                    messages.SUCCESS,
                    'You have successfully updated your practice session.')
            return redirect(f"/practice/{session_id}")
        else:
            return render(
                request,
                'editlog.html',
                {"form": form}
            )
