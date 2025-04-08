from django.test import TestCase
from django.urls import reverse



# Create your tests here.
class HomeTests(TestCase):

    # Ensuring the home page loads
    def test_home_status_code(self):
        response = self.client.get(reverse('home.index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')
