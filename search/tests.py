from django.test import TestCase, SimpleTestCase
from django.urls import reverse



# Create your tests here.
class searchPage(TestCase):

    def search_status_code(self):
        response = self.client.get(reverse('restaurantSoftware:search'))
        self.assertEqual(response.status_code, 200)
