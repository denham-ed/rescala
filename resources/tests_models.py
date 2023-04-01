from django.test import TestCase, Client
from .models import Resource


# ----------------------------------------------- Resource Model
class TestResourceModel(TestCase):
    def setUp(self):
        self.resource = Resource.objects.create(
            title="Test Resource",
            slug="test-resource",
            content="This is a test resource.",
            excerpt="Test excerpt",
            status=0
        )

    def test_string_title_of_resource(self):
        self.assertEqual(str(self.resource), "Test Resource")

    def tearDown(self):
        self.resource.delete()