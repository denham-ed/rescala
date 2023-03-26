from django.test import TestCase, Client
from users.models import Profile
from django.shortcuts import reverse

class TestDashboardView(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.client = Client()
        cls.url = reverse('dashboard')
        cls.user = Profile.objects.create_user(
            username='testuser',
            password='testpass',
        )

    def test_user_can_view_dashboard(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard.html')

    # def test_dashboard_context_is_present(self):

    def test_anonymous_user_is_redirected(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)


    @classmethod
    def tearDownClass(cls):
        cls.user.delete()
        super().tearDownClass()

