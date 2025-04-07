from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your tests here.
class ResultsTests(TestCase):
    def loggedIn(self):
        self.user = get_user_model().objects.create_user(
            username='testuser', password='testpassword'
        )

        self.client.login(username='testuser', password='testpassword')

    def results_status_code(self):
        response = self.client.get(reverse('restaurantSoftware:results'))
        self.assertEqual(response.status_code, 200)