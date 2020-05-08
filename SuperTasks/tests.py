"Tests for any functionality outside of an 'app'"
from django.test import TestCase
from django.urls import reverse

# Create your tests here.

class IndexViewTests(TestCase):
    "Tests for the index page i.e. the URL '/' "

    def test_not_logged_in_redirect(self):
        """
        If a user accesses the root page '/'
        with not being logged in, they should
        redirect to '/accounts/login'
        """
        index_url = reverse('index')
        login_url = '/accounts/login'

        response = self.client.get(index_url)

        self.assertRedirects(response, f'{login_url}/?next={index_url}')
