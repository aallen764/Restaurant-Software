from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class AccountPageTests(TestCase):
    
    # creates a test user object to be used in future accountPage tests
    # username: "testuser"; password: "testpass"
    # calls accountPage view
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.url = reverse('account.index')

    # first test case:
    # checks if account page is visited by an AUTHENTICATED user
    # logs in test user using credentials created above
    # gets and checks status code to make sure it's set to 200
    # lastly, checks that we are on the account page by looking for the beginning of our welcome message, displayed in the account page
    def test_account_page_for_authenticated_user(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Welcome,')  # assuming "Welcome," is part of the content of the page

    # second test case:
    # checks if account page is visited by an UNAUTHENTICATED USER
    # calls the account page url
    # due to user being signed-out, they are then redirected back to the home page ('/')
    def test_account_page_for_unauthenticated_user(self):
        response = self.client.get(self.url)
        self.assertRedirects(response, '/')
