from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class HomeTests(TestCase):
    def home_status_code(self):
        response = self.client.get(reverse('restaurantSoftware:home'))
        self.assertEqual(response.status_code, 200)
