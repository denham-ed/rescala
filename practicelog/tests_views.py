from django.test import TestCase, Client
from users.models import Profile
from .models import Session
# from resources.models import Resource
from django.shortcuts import reverse
from users.forms import GoalForm
from datetime import datetime
from django.contrib.messages import get_messages
from .forms import CreateSessionForm


class TestDashboardView(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.client = Client()
        cls.url = reverse('dashboard')
        cls.user = Profile.objects.create_user(
            username='testuser',
            password='testpass',
            goals=[{'goal': 'Create First Tests', 'complete': 0}]
        )
        cls.session1 = Session.objects.create(
            user=cls.user,
            headline="Session for Unit Testing",
            date=datetime.strptime('2023-03-25', '%Y-%m-%d'),
            duration=30,
            focus=["rhythm", "sightreading"],
            moods=["inspired", "determined"],
            summary="Testing Session",
        )
        cls.session2 = Session.objects.create(
            user=cls.user,
            headline="Session for Unit Testing",
            date=datetime.strptime('2023-03-24', '%Y-%m-%d'),
            duration=30,
            focus=["rhythm", "sightreading"],
            moods=["determined"],
            summary="Testing Session2",
        )

    def test_user_can_view_dashboard(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard.html')

    def test_goals_context_is_provided(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(self.url)
        self.assertEqual(response.context['goals'], self.user.goals)
        self.assertIsInstance(response.context['goalform'], GoalForm)

    def test_sessions_context_is_provided(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(self.url)
        self.assertEqual(
            list(response.context['sessions']),
            [self.session1, self.session2])

    def test_add_goal_form_is_valid(self):
        form_data = {
            "goal_name": "Perfect unit testing for Django"
        }
        form = GoalForm(data=form_data)
        self.assertEqual(form.is_valid(), True)

    def test_new_goal_is_added_to_user_goals(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(
            reverse('add_goal'),
            {'goal_name': "A user-added goal"}
            )
        self.user.refresh_from_db()
        self.assertEqual(len(self.user.goals), 2)
        added_goal = self.user.goals[1]
        self.assertEqual(added_goal['goal'], "A user-added goal")
        self.assertEqual(added_goal['complete'], 0)

    def test_add_goal_redirects_to_dashboard(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(
            reverse('add_goal'),
            {'goal_name': "A user-added goal"}
            )
        self.assertEqual(response.status_code, 302)

    def test_add_goal_displays_message_on_success(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(
            reverse('add_goal'),
            {'goal_name': "A user-added goal"}
            )
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'You have added a long term goal!')

    # Update Goal
    def test_updated_goal_is_saved(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(
            reverse('update_goal', args=[0]),
            {'goal_id': '0', 'goal-complete': 100})
        self.user.refresh_from_db()
        added_goal = self.user.goals[0]
        self.assertEqual(added_goal['goal'], "Create First Tests")
        self.assertEqual(added_goal['complete'], '100')

    def test_update_goal_displays_message_on_success(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(
            reverse('update_goal', args=[0]),
            {'goal_id': '0', 'goal-complete': 100})
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(
            str(messages[0]),
            'You have updated a long term goal.')

    def test_add_goal_redirects_to_dashboard(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(
            reverse('update_goal', args=[0]),
            {'goal_id': '0', 'goal-complete': 100})
        self.assertEqual(response.status_code, 302)

    # Authentication
    def test_anonymous_user_is_redirected(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)

    @classmethod
    def tearDownClass(cls):
        cls.user.delete()
        super().tearDownClass()


class TestCreateSessionView(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.client = Client()
        cls.user = Profile.objects.create_user(
            username='testuser',
            password='testpass',
            goals=[{'goal': 'Create First Tests', 'complete': 0}]
        )
        cls.url = reverse('create_log')
        cls.form_data = {
            "headline": "View Testing Session",
            "date": '2023-01-01',
            "duration": 30,
            "focus": ["rhythm", "sightreading"],
            "moods": ["inspired", "determined"],
            "summary": "I had a great session today",
        }

    def test_user_can_view_create_session_page(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'createlog.html')

    def test_form_context_is_provided(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(self.url)
        self.assertIsInstance(response.context['form'], CreateSessionForm)

    # Test Post Method
    def test_valid_create_session_form_creates_session(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(
            reverse('create_log'), data=self.form_data)
        sessions = Session.objects.filter(headline=self.form_data['headline'])
        self.assertEqual(len(sessions), 1)

    def test_create_session_form_redirects_to_dashboard_on_success(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(
            reverse('create_log'), data=self.form_data)
        self.assertRedirects(response, reverse('dashboard'))

    def test_invalid_create_session_form_redirects(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(
            reverse('create_log'), data={})
        self.assertTemplateUsed(response, 'createlog.html')
    
    def test_create_session_displays_message_on_success(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(
            reverse('create_log'), data=self.form_data)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(
            str(messages[0]),
            'Your practice has been logged successfully.')
        
    # Authentication
    def test_anonymous_user_is_redirected(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)

    @classmethod
    def tearDownClass(cls):
        cls.user.delete()
        super().tearDownClass()