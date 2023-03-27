from django.test import TestCase, Client
from .forms import CreateSessionForm
from users.models import Profile
from django.shortcuts import reverse
from datetime import datetime

# Set Up Class to log in/out??
class TestCreateLogView(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('create_log')
        self.user = Profile.objects.create_user(
            username='testuser',
            password='testpass',
        )

    def test_anonymous_user_is_redirected(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)

    def test_user_can_view_create_log_form(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'createlog.html')

    def test_create_log_form_renders(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(self.url)
        self.assertIsInstance(response.context['form'], CreateSessionForm)

    def tearDown(self):
        self.user.delete()






# Edit Session Form