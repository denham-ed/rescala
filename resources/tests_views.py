from django.test import TestCase, Client
from users.models import Profile
from django.shortcuts import reverse
from .models import Resource
from datetime import datetime


class TestResourcesPage(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.client = Client()
        cls.url = reverse('resources')

    def test_all_users_can_view_page(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('resources.html')

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()


class TestResourceDetailsView(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.client = Client()
        cls.resource = Resource.objects.create(
            title='Test Resource',
            content='Test Content',
            excerpt='Test Excerpt',
            created_on=datetime.today(),
            status=1
        )
        cls.user = Profile.objects.create_user(
            username='testuser',
            password='testpass',
        )

    def test_resource_is_provided_as_context(self):
        response = self.client.get(reverse('resource_details', args=[self.resource.id]))
        self.assertEqual(response.context['resource'], self.resource)

    def test_recommended_reading_is_provided(self):
        response = self.client.get(reverse('resource_details', args=[self.resource.id]))
        articles = Resource.objects.exclude(id=self.resource.id).filter(status=1)
        self.assertQuerysetEqual(response.context['articles'], articles[:3])

    def test_not_favourite_article_shown_as_not_favourite(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('resource_details', args=[self.resource.id]))
        self.assertEqual(response.context['favourite'], False)

    def test_favourite_article_shown_as_favourite(self):
        self.client.login(username='testuser', password='testpass')
        self.user.resources.set([self.resource])
        response = self.client.get(reverse('resource_details', args=[self.resource.id]))
        self.assertEqual(response.context['favourite'], True)

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()

