from django.test import TestCase, SimpleTestCase
from django.urls import reverse



# Create your tests here.
class searchPage(TestCase):

    def test_search_status_code(self):
        response = self.client.get(reverse('search:index'))
        self.assertEqual(response.status_code, 200)
