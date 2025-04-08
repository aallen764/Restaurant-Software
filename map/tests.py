from django.test import TestCase, SimpleTestCase
from unittest import TestCase
from django.urls import reverse

# Create your tests here.
class MapUrlTest(SimpleTestCase):
    def testMapUrl(self):
        response = self.client.get(reverse('map.index'))

        #This checks if when the page is ran that it returns a 200 stustua code which stands for 'OK'
        self.assertEqual(response.status_code, 200)

        #This checks if the page contains an div with the ID map which indicates that the map has loaded 
        self.assertContains(response, 'id="map"')