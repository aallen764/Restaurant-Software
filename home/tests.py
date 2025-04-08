<<<<<<< HEAD
from django.test import TestCase, Client
from django.urls import reverse

class HomePageTests(TestCase):
    def setUp(self):
        # Create a test client to simulate a browser
        self.client = Client()

    def test_home_index_view_status_code(self):
        # Check that the homepage responds with HTTP 200 (OK)
        response = self.client.get(reverse('home.index'))
        self.assertEqual(response.status_code, 200)

    def test_home_index_template_used(self):
        # Check that the homepage uses the correct template
        response = self.client.get(reverse('home.index'))
        self.assertTemplateUsed(response, 'home/index.html')

    def test_home_index_context_data(self):
        # Check that the context contains the correct title
        response = self.client.get(reverse('home.index'))
        self.assertIn('template_data', response.context)
        self.assertEqual(response.context['template_data']['title'], 'BiteFinder')
=======
from django.test import TestCase
from django.urls import reverse



# Create your tests here.
class HomeTests(TestCase):

    # Ensuring the home page loads
    def test_home_status_code(self):
        response = self.client.get(reverse('home.index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')
>>>>>>> release/feb11
