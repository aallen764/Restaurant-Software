from django.test import TestCase, Client
from unittest import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import user_Profile

USER_MODEL = get_user_model()

# Create your tests here.
class SignUpClientTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('signUp')

    def testSignUp(self):
        data = {
            'username': 'fake_user',
            'password': 'fakebaddie',
            'email_address': 'fakeuser@gmail.com',  
            'phone_number': '8764649107',
            'zip_code': '10013'
        }

        response = self.client.post(self.url, data)

        person = USER_MODEL.objects.get(username='fake_user')

        self.assertEqual(response.status_code, 200)
        self.assertTrue(USER_MODEL.objects.filter(username='fake_user').exists())




