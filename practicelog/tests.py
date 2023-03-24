from django.test import TestCase, Client
from .forms import CreateSessionForm
from users.models import Profile
# from django.urls import reverse
from django.shortcuts import reverse


class TestCreateLogView(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('create_log')
        self.user = Profile.objects.create_user(
            username='testuser',
            password='testpass',
        )

    def test_get(self):
        loggedin = self.client.login(username='testuser', password='testpass')
        print(loggedin)
        response = self.client.get(self.url, follow=True)
        self.assertEqual(response.status_code, 200)
        # self.assertTemplateUsed(response, 'createlog.html')
        # self.assertIsInstance(response.context['form'], CreateSessionForm)

    def tearDown(self):
        self.user.delete()
