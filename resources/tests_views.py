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
        cls.user = Profile.objects.create_user(
            username='testuser',
            password='testpass',
        )
        cls.resource = Resource.objects.create(
            title='Test Resource',
            content='Test Content',
            excerpt='Test Excerpt',
            created_on=datetime.today(),
            status=1
        )

    def test_resource_is_provided_as_context(self):
        print(self.resource)
        response = self.client.get(reverse('resource_details', args=[self.resource.id]))
        self.assertEqual(response.context['resource'], self.resource)


    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()

