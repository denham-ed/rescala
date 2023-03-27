from django.test import TestCase, Client
from users.models import Profile
from .models import Session
# from resources.models import Resource
from django.shortcuts import reverse
from users.forms import GoalForm
from datetime import datetime

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
        self.assertEqual(list(response.context['sessions']), [self.session1, self.session2])

    def test_add_goal_form_is_valid(self):
        form_data = {
            "goal_name":"Perfect unit testing for Django"
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




    # def test_sessions__list_provied_if_empty(self):
    #     self.session1.delete()
    #     self.session2.delete()
    #     self.client.login(username='testuser', password='testpass')
    #     response = self.client.get(self.url)
    #     self.assertQuerysetEqual(response.context['sessions'],[])





    # def test_add_goal_displays_message_on_success(self):


    def test_anonymous_user_is_redirected(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)


    @classmethod
    def tearDownClass(cls):
        cls.user.delete()
        super().tearDownClass()

