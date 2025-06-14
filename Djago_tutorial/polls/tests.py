from django.test import TestCase
from django.urls import reverse, resolve
from django.http import HttpRequest
from .views import index  

class HomepageTest(TestCase):

    def test_homepage_url_exists(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_homepage_url_by_name(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_homepage_uses_correct_template(self):
        response = self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'index.html')  

    def test_homepage_contains_expected_content(self):
        response = self.client.get(reverse('index'))
        self.assertContains(response, "Welcome")  

    def test_homepage_does_not_contain_unexpected_content(self):
        response = self.client.get(reverse('index'))
        self.assertNotContains(response, "Error")

    def test_homepage_view_function(self):
        found = resolve('/')
        self.assertEqual(found.func, index)  

    def test_404_on_invalid_url(self):
        response = self.client.get('/nonexistent/')
        self.assertEqual(response.status_code, 404)

