from django.test import TestCase, Client
from .forms import CreateSessionForm, EditSessionForm
from users.models import Profile
from .models import Session
from django.shortcuts import reverse
from datetime import datetime

# Create Session Log Form
class TestCreateSessionForm(TestCase):
    def setUp(self):
        self.client = Client()
        # self.url = reverse('create_log')
        self.user = Profile.objects.create_user(
            username='testuser',
            password='testpass',
        )
        self.form_data = {
            "headline": "My practice session",
            "date": datetime.strptime('2023-01-01', '%Y-%m-%d'),
            "duration": 30,
            "focus": ["rhythm", "sightreading"], 
            "moods": ["inspired", "determined"],
            "summary": "I had a great session today",
        }

    def test_form_is_valid(self):
        self.client.login(username='testuser', password='testpass')
        form = CreateSessionForm(data=self.form_data)
        self.assertEqual(form.is_valid(), True)

    def test_blank_headline(self):
        form_data = {
            **self.form_data,
            "headline":""
        }
        form = CreateSessionForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('headline', form.errors)

    def test_blank_duration(self):
        form_data = {
            **self.form_data,
            "duration":""
        }
        form = CreateSessionForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('duration', form.errors)

    def test_negative_duration(self):
        form_data = {
            **self.form_data,
            "duration": -10
        }
        form = CreateSessionForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('duration', form.errors)
    
    def test_duration_too_high(self):
        form_data = {
            **self.form_data,
            "duration": 361
        }
        form = CreateSessionForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('duration', form.errors)

    def test_blank_summary(self):
        form_data = {
            **self.form_data,
            "summary": ""
        }
        form = CreateSessionForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('summary', form.errors)

    def test_empty_moods_is_valid(self):
        form_data = {
            **self.form_data,
            "moods": []
        }
        form = CreateSessionForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_empty_focus_is_valid(self):
        form_data = {
            **self.form_data,
            "focus": []
        }
        form = CreateSessionForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_future_date_is_invalid(self):
        form_data = {
            **self.form_data,
            "date": datetime.strptime('2024-01-01', '%Y-%m-%d'),
        }
        form = CreateSessionForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('date', form.errors)

    def tearDown(self):
        self.user.delete()

# --------------------------------------------- Edit Sessions
class TestEditSessionForm(TestCase):
    def setUp(self):
        self.client = Client()

        self.user = Profile.objects.create_user(
            username='testuser',
            password='testpass',
        )
        self.session = Session.objects.create(
            user= self.user,
            headline="Session for Unit Testing",
            date=datetime.strptime('2023-01-01', '%Y-%m-%d'),
            duration=30,
            focus=["rhythm", "sightreading"],
            moods=["inspired", "determined"],
            summary="Testing Session",
        )
        self.form_data = {
            "headline": "My practice session",
            "date": datetime.strptime('2023-01-01', '%Y-%m-%d'),
            "duration": 30,
            "focus": ["rhythm", "sightreading"], 
            "moods": ["inspired", "determined"],
            "summary": "I had a great session today",
        }


    def test_form_is_valid(self):
        form = EditSessionForm(session=self.session, data=self.form_data)
        self.assertEqual(form.is_valid(), True)

    def test_blank_headline(self):
        form_data = {
            **self.form_data,
            "headline":""
        }
        form = EditSessionForm(session=self.session, data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('headline', form.errors)

    def test_blank_duration(self):
        form_data = {
            **self.form_data,
            "duration":""
        }
        form = EditSessionForm(session=self.session, data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('duration', form.errors)

    def test_negative_duration(self):
        form_data = {
            **self.form_data,
            "duration": -10
        }
        form = EditSessionForm(session=self.session, data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('duration', form.errors)
    
    def test_duration_too_high(self):
        form_data = {
            **self.form_data,
            "duration": 361
        }
        form = EditSessionForm(session=self.session, data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('duration', form.errors)

    def test_blank_summary(self):
        form_data = {
            **self.form_data,
            "summary": ""
        }
        form = EditSessionForm(session=self.session, data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('summary', form.errors)

    def test_empty_moods_is_valid(self):
        form_data = {
            **self.form_data,
            "moods": []
        }
        form = EditSessionForm(session=self.session, data=form_data)
        self.assertTrue(form.is_valid())

    def test_empty_focus_is_valid(self):
        form_data = {
            **self.form_data,
            "focus": []
        }
        form = EditSessionForm(session=self.session, data=form_data)
        self.assertTrue(form.is_valid())

    def test_future_date_is_invalid(self):
        form_data = {
            **self.form_data,
            "date": datetime.strptime('2024-01-01', '%Y-%m-%d'),
        }
        form = EditSessionForm(session=self.session, data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('date', form.errors)

    def tearDown(self):
        self.user.delete()
        