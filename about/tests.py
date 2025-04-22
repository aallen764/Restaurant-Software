from django.test import TestCase, Client
from django.urls import reverse

class AboutPageTests(TestCase):
    def setUp(self):
        # Set up a test client that simulates a web browser
        self.client = Client()

    def test_about_index_view_status_code(self):
        # Test that the about index page loads successfully (HTTP 200)
        response = self.client.get(reverse('about.index'))
        self.assertEqual(response.status_code, 200)

    def test_about_index_template_used(self):
        # Test that the view renders the correct template
        response = self.client.get(reverse('about.index'))
        self.assertTemplateUsed(response, 'about/index.html')

    def test_about_index_context_data(self):
        # Test that the 'title' in the context is correctly set to "About"
        response = self.client.get(reverse('about.index'))
        self.assertIn('template_data', response.context)
        self.assertEqual(response.context['template_data']['title'], 'About')