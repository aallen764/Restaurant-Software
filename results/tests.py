from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your tests here.
class ResultsTests(TestCase):
    def test_loggedIn(self):
        self.user = get_user_model().objects.create_user(
            username='testuser', password='testpassword'
        )

        self.client.login(username='testuser', password='testpassword')

    def test_results_status_code(self):
        response = self.client.get(reverse('results:index'))
        self.assertEqual(response.status_code, 200)