from django.test import TestCase, Client
from datetime import datetime
from django.contrib.messages import get_messages
from django.shortcuts import reverse
from users.forms import GoalForm
from users.models import Profile
from .forms import CreateSessionForm, EditSessionForm
from .models import Session


# -------------------------------------- Test Dashboard View
class TestDashboardView(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.client = Client()
        cls.url = reverse("dashboard")
        cls.user = Profile.objects.create_user(
            username="testuser",
            password="testpass",
            goals=[{"goal": "Create First Tests", "complete": 0}],
        )
        cls.session1 = Session.objects.create(
            user=cls.user,
            headline="Session for Unit Testing",
            date=datetime.strptime("2023-03-25", "%Y-%m-%d"),
            duration=30,
            focus=["rhythm", "sightreading"],
            moods=["inspired", "determined"],
            summary="Testing Session",
        )
        cls.session2 = Session.objects.create(
            user=cls.user,
            headline="Session for Unit Testing",
            date=datetime.strptime("2023-03-24", "%Y-%m-%d"),
            duration=30,
            focus=["rhythm", "sightreading"],
            moods=["determined"],
            summary="Testing Session2",
        )

    def test_user_can_view_dashboard(self):
        self.client.login(username="testuser", password="testpass")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "dashboard.html")

    def test_goals_context_is_provided(self):
        self.client.login(username="testuser", password="testpass")
        response = self.client.get(self.url)
        self.assertEqual(response.context["goals"], self.user.goals)
        self.assertIsInstance(response.context["goalform"], GoalForm)

    def test_sessions_context_is_provided(self):
        self.client.login(username="testuser", password="testpass")
        response = self.client.get(self.url)
        self.assertEqual(
            list(response.context["sessions"]), [self.session1, self.session2]
        )

    def test_add_goal_form_is_valid(self):
        form_data = {"goal_name": "Perfect unit testing for Django"}
        form = GoalForm(data=form_data)
        self.assertEqual(form.is_valid(), True)

    def test_new_goal_is_added_to_user_goals(self):
        self.client.login(username="testuser", password="testpass")
        response = self.client.post(
            reverse("add_goal"), {"goal_name": "A user-added goal"}
        )
        self.user.refresh_from_db()
        self.assertEqual(len(self.user.goals), 2)
        added_goal = self.user.goals[1]
        self.assertEqual(added_goal["goal"], "A user-added goal")
        self.assertEqual(added_goal["complete"], 0)

    def test_add_goal_redirects_to_dashboard(self):
        self.client.login(username="testuser", password="testpass")
        response = self.client.post(
            reverse("add_goal"), {"goal_name": "A user-added goal"}
        )
        self.assertEqual(response.status_code, 302)

    def test_add_goal_displays_message_on_success(self):
        self.client.login(username="testuser", password="testpass")
        response = self.client.post(
            reverse("add_goal"), {"goal_name": "A user-added goal"}
        )
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), "You have added a long term goal!")

    def test_add_goal_form_is_invalid(self):
        form_data = {"goal_name": ""}
        form = GoalForm(data=form_data)
        self.assertEqual(form.is_valid(), False)

    def test_invalid_add_goal_form_redirects(self):
        self.client.login(username="testuser", password="testpass")
        response = self.client.post(reverse("add_goal"), {"goal_name": ""})
        self.assertEqual(response.status_code, 302)

    def test_add_goal_displays_message_on_invalid_form(self):
        self.client.login(username="testuser", password="testpass")
        response = self.client.post(reverse("add_goal"), {"goal_name": ""})
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(
            str(messages[0]),
            "Oops - you need to enter a goal. Please try again."
        )

    def test_updated_goal_is_saved(self):
        self.client.login(username="testuser", password="testpass")
        response = self.client.post(
            reverse("update_goal", args=[0]),
            {"goal_id": "0", "goal-complete": 100}
        )
        self.user.refresh_from_db()
        added_goal = self.user.goals[0]
        self.assertEqual(added_goal["goal"], "Create First Tests")
        self.assertEqual(added_goal["complete"], "100")

    def test_update_goal_displays_message_on_success(self):
        self.client.login(username="testuser", password="testpass")
        response = self.client.post(
            reverse("update_goal", args=[0]),
            {"goal_id": "0", "goal-complete": 100}
        )
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(
            str(messages[0]),
            "You have updated a long term goal.")

    def test_update_goal_redirects_to_dashboard(self):
        self.client.login(username="testuser", password="testpass")
        response = self.client.post(
            reverse("update_goal", args=[0]),
            {"goal_id": "0", "goal-complete": 100}
        )
        self.assertEqual(response.status_code, 302)

    def test_delete_goal_removes_goal_from_user(self):
        self.client.login(username="testuser", password="testpass")
        self.client.post(
            reverse("add_goal"),
            {"goal_name": "Goal for deleting"})
        self.user.refresh_from_db()
        response = self.client.post(reverse("delete_goal", args=[1]))
        self.user.refresh_from_db()
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(self.user.goals), 1)
        self.assertEqual(len(messages), 2)
        self.assertEqual(
            str(messages[1]),
            "You have removed a long term goal.")

    def test_anonymous_user_is_redirected(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)

    @classmethod
    def tearDownClass(cls):
        cls.user.delete()
        super().tearDownClass()


# -------------------------------------- Test Create Session View
class TestCreateSessionView(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.client = Client()
        cls.user = Profile.objects.create_user(
            username="testuser",
            password="testpass",
            goals=[{"goal": "Create First Tests", "complete": 0}],
        )
        cls.url = reverse("create_log")
        cls.form_data = {
            "headline": "View Testing Session",
            "date": "2023-01-01",
            "duration": 30,
            "focus": ["rhythm", "sightreading"],
            "moods": ["inspired", "determined"],
            "summary": "I had a great session today",
        }

    def test_user_can_view_create_session_page(self):
        self.client.login(username="testuser", password="testpass")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "createlog.html")

    def test_form_context_is_provided(self):
        self.client.login(username="testuser", password="testpass")
        response = self.client.get(self.url)
        self.assertIsInstance(response.context["form"], CreateSessionForm)

    def test_valid_create_session_form_creates_session(self):
        self.client.login(username="testuser", password="testpass")
        response = self.client.post(reverse("create_log"), data=self.form_data)
        sessions = Session.objects.filter(headline=self.form_data["headline"])
        self.assertEqual(len(sessions), 1)

    def test_create_session_form_redirects_to_dashboard_on_success(self):
        self.client.login(username="testuser", password="testpass")
        response = self.client.post(reverse("create_log"), data=self.form_data)
        self.assertRedirects(response, reverse("dashboard"))

    def test_invalid_create_session_form_rerenders(self):
        self.client.login(username="testuser", password="testpass")
        response = self.client.post(reverse("create_log"), data={})
        self.assertTemplateUsed(response, "createlog.html")

    def test_create_session_displays_message_on_success(self):
        self.client.login(username="testuser", password="testpass")
        response = self.client.post(reverse("create_log"), data=self.form_data)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(
            str(messages[0]), "Your practice has been logged successfully."
        )

    def test_anonymous_user_is_redirected(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)

    @classmethod
    def tearDownClass(cls):
        cls.user.delete()
        super().tearDownClass()


# -------------------------------------- Test Session Details View
class TestSessionDetailsView(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.client = Client()

        cls.user = Profile.objects.create_user(
            username="testuser",
            password="testpass",
        )
        cls.session = Session.objects.create(
            user=cls.user,
            headline="Session with Session Details",
            date=datetime.strptime("2023-03-25", "%Y-%m-%d"),
            duration=60,
            focus=["performing", "technique"],
            moods=["anxious", "ambitious"],
            summary="Session with Session Details Summary",
        )

    def test_user_can_view_session_details_page(self):
        url = reverse("session_details", args=[self.session.id])
        self.client.login(username="testuser", password="testpass")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "sessiondetails.html")

    def test_session_is_provided_as_context(self):
        url = reverse("session_details", args=[self.session.id])
        session = Session.objects.filter(id=self.session.id)[0]
        self.client.login(username="testuser", password="testpass")
        response = self.client.get(url)
        self.assertEqual(response.context["session"], session)

    def test_anonymous_user_is_redirected(self):
        url = reverse("session_details", args=[self.session.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_delete_session_removes_session_from_db(self):
        self.client.login(username="testuser", password="testpass")
        response = self.client.post(reverse(
            "delete_session",
            args=[self.session.id]))
        self.assertFalse(Session.objects.filter(id=self.session.id).exists())

    def test_user_redirected_after_deleting_session(self):
        self.client.login(username="testuser", password="testpass")
        response = self.client.post(reverse(
            "delete_session",
            args=[self.session.id]))
        self.assertEqual(response.status_code, 302)

    @classmethod
    def tearDownClass(cls):
        cls.user.delete()
        super().tearDownClass()


# -------------------------------------- Test Edit Session View
class TestEditSessionView(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.client = Client()
        cls.user = Profile.objects.create_user(
            username="testuser",
            password="testpass")
        cls.url = reverse("create_log")
        cls.edit_form_data = {
            "headline": "Edited  Session",
            "date": "2023-01-01",
            "duration": 30,
            "focus": ["rhythm", "sightreading"],
            "moods": ["inspired", "determined"],
            "summary": "Edited Summary",
        }

    def setUp(self):
        self.session = Session.objects.create(
            user=self.user,
            headline="Session for Edit Session",
            date=datetime.strptime("2023-03-25", "%Y-%m-%d"),
            duration=60,
            focus=["performing", "technique"],
            moods=["anxious", "ambitious"],
            summary="Session with Session Details Summary",
        )


    def test_user_can_view_edit_session_page(self):
        self.client.login(username="testuser", password="testpass")
        response = self.client.get(reverse(
            "edit_session",
            args=[self.session.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "editlog.html")

    def test_context_is_provided(self):
        self.client.login(username="testuser", password="testpass")
        response = self.client.get(reverse(
            "edit_session",
            args=[self.session.id]))
        self.assertIsInstance(response.context["form"], EditSessionForm)
        self.assertEqual(response.context["session"], self.session)

    def test_initial_values_in_form(self):
        self.client.login(username="testuser", password="testpass")
        response = self.client.get(reverse(
            "edit_session",
            args=[self.session.id]))
        initial_values = {
            "headline": self.session.headline,
            "date": self.session.date.strftime("%Y-%m-%d"),
            "duration": self.session.duration,
            "focus": self.session.focus,
            "summary": self.session.summary,
            "moods": self.session.moods,
        }
        form = response.context["form"]
        self.assertEqual(form.initial["headline"], initial_values["headline"])
        self.assertEqual(form.initial["date"], initial_values["date"])
        self.assertEqual(form.initial["duration"], initial_values["duration"])
        self.assertEqual(form.initial["focus"], initial_values["focus"])
        self.assertEqual(form.initial["summary"], initial_values["summary"])
        self.assertEqual(form.initial["moods"], initial_values["moods"])

    def test_valid_edit_session_form_updates_session(self):
        self.client.login(username="testuser", password="testpass")
        response = self.client.post(reverse(
            "edit_session",
            args=[self.session.id]), data=self.edit_form_data)
        sessions = Session.objects.filter(id=self.session.id)
        session = Session.objects.get(id=self.session.id)
        self.assertEqual(session.headline, self.edit_form_data["headline"])
        self.assertEqual(
            session.date,
            datetime.strptime(self.edit_form_data["date"], "%Y-%m-%d").date(),
        )
        self.assertEqual(session.duration, self.edit_form_data["duration"])
        self.assertEqual(session.focus, self.edit_form_data["focus"])
        self.assertEqual(session.summary, self.edit_form_data["summary"])
        self.assertEqual(session.moods, self.edit_form_data["moods"])

    def test_invalid_form_rerenders_edit_session_view(self):
        self.client.login(username="testuser", password="testpass")
        response = self.client.post(
            reverse("edit_session", args=[self.session.id]), data={}
        )
        self.assertTemplateUsed(response, "editlog.html")

    def test_anonymous_user_is_redirected(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)

    def tearDown(self):
        self.session.delete()

    @classmethod
    def tearDownClass(cls):
        cls.user.delete()
        super().tearDownClass()
