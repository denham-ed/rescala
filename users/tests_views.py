from django.test import TestCase, Client
from django.shortcuts import reverse
from .models import Profile


# ---------------------------------------------- Landing Page View
class TestLandingPageView(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.user = Profile.objects.create_user(
            username='testuser',
            password='testpass',
        )
    
    def test_logged_in_user_redirects_to_dashboard(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('landing_page'))
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed('dashboard.html')
   
    def test_anonymous_user_can_view_landing(self):
        self.client.logout()
        response = self.client.get(reverse('landing_page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('landing.html')
    
    def tearDown(self):
        self.user.delete()
