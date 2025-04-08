from django.test import TestCase, SimpleTestCase
from django.urls import reverse
from django.contrib.auth import get_user_model



# Create your tests here.
class searchPage(TestCase):

    # testing the form submission to results page
    def test_search_form_submission(self):
        # make sure the user is logged in
        self.user = get_user_model().objects.create_user(
            username='testuser', password='testpassword'
        )
        self.client.login(username='testuser', password='testpassword')

        # Fake form with test data
        form_data = {
            'query': 'pizza', 
            'nearby': 'on', 
            'open': 'on',   
            'Bar': 'on',     
        }

        # send this to the results page
        response = self.client.get(reverse('results.index'), data=form_data)
        # make sure the result page still loads with this information
        self.assertEqual(response.status_code, 200)

    # Ensuring the search page loads
    def test_search_status_code(self):
        response = self.client.get(reverse('search.index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'search/index.html')
