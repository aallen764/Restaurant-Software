from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from signUp.models import user_Profile
from accountPage import updater


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
        
        
        
        
        
        



class AccountUpdaterTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="tester", password="pass123")
        self.user_profile = self.user.user_profile
        self.user_profile.email_address = "tester@example.com"
        self.user_profile.phone_number = "1234567890"
        self.user_profile.zip_code = "12345"
        self.user_profile.save()

    def test_update_username_success(self):
        response = updater.update_username(self.user.id, "newtester")
        self.assertEqual(response, "Username updated successfully.")
        self.user.refresh_from_db()
        self.assertEqual(self.user.username, "newtester")

    def test_update_username_taken(self):
        User.objects.create_user(username="taken", password="abc")
        response = updater.update_username(self.user.id, "taken")
        self.assertEqual(response, "Username already taken.")

    def test_update_password(self):
        response = updater.update_password(self.user.id, "newpassword")
        self.assertEqual(response, "Password updated successfully.")
        self.assertTrue(User.objects.get(id=self.user.id).check_password("newpassword"))

    def test_update_email_success(self):
        response = updater.update_email(self.user.id, "new@example.com")
        self.assertEqual(response, "Email updated successfully.")
        self.user_profile.refresh_from_db()
        self.assertEqual(self.user_profile.email_address, "new@example.com")

    def test_update_email_taken(self):
        other_user = User.objects.create_user(username="other", password="abc")
        other_user.user_profile.email_address = "duplicate@example.com"
        other_user.user_profile.save()
        response = updater.update_email(self.user.id, "duplicate@example.com")
        self.assertEqual(response, "Email already in use.")

    def test_update_zip_valid(self):
        response = updater.update_zip(self.user.id, "54321")
        self.assertEqual(response, "Zip code updated successfully.")
        self.user_profile.refresh_from_db()
        self.assertEqual(self.user_profile.zip_code, "54321")

    def test_update_zip_invalid(self):
        response = updater.update_zip(self.user.id, "abc")
        self.assertEqual(response, "Invalid zip code format. Must be 5–10 digits.")
