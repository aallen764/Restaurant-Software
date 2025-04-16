from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse

class LoginTestCase(TestCase):

    def setUp(self):  # create a testing environment (client) that builds a test user object -> user: "testuser" ; password: "testpass123" to be used in test cases
        self.client = Client()
        self.username = "testuser"
        self.password = "testpass123"
        self.user = User.objects.create_user(username=self.username, password=self.password)  # create test user object
        self.url = reverse('login.index')  # Set URL for the login page

    # first test case:
    # tests if test user can successfully login (tests if user fields are valid and exist in the database)
    # calls the login index view and inputs the test username and test password into their respective fields
    # reirects and verifies that the user was sent to the homepage ('/')
    # lastly, checks that the user is logged in by checking authentication id
    def test_login_success(self):
        response = self.client.post(self.url, {
            'username': self.username,  # Using the setUp method's username
            'password': self.password
        })

        self.assertRedirects(response, '/')
        self.assertTrue('_auth_user_id' in self.client.session)

    # second test case:
    # tests if user fails to login when using incorrect credentials (username and/or password)
    # calls login view to begin login process
    # inputs the correct username generated & assigned to the test user object in setUp(self)
    # inputs an INCORRECT password: "thisiswrong"
    # checks if user is successfully brought back to the home page
    # outputs error message describing cause of error
    def test_login_failure(self):
        response = self.client.post(self.url, {
            'username': self.username,
            'password': 'thisiswrong'
        })

        self.assertRedirects(response, '/')
        messages = list(response.wsgi_request._messages)
        self.assertTrue(any("Invalid username or password" in str(m) for m in messages))

    # third test case:
    # tests if the login page correct loads when login.index is called
    # calls the login index froms login/views.py
    # checks for the correct status code (200)
    # lastly, if correct status code is shown, checks if the correct template (html) is loaded from the view
    def test_login_page_loads(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login/login2.html')
