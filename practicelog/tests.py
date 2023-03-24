from django.test import TestCase, Client
from .forms import CreateSessionForm
from users.models import Profile
from django.shortcuts import reverse
from datetime import datetime


class TestCreateLogView(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('create_log')
        self.user = Profile.objects.create_user(
            username='testuser',
            password='testpass',
        )

    def test_user_can_view_create_log_form(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(self.url, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'createlog.html')

    def test_create_log_form_renders(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(self.url, follow=True)
        self.assertIsInstance(response.context['form'], CreateSessionForm)

    def tearDown(self):
        self.user.delete()


class TestCreateLogForm(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('create_log')
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


    # def test_blank_required_fields(self):

    #     self.assertIn('date', form.errors)



    def tearDown(self):
        self.user.delete()
