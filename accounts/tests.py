from django.test import TestCase
from django.contrib.auth.models import User
from .models import Account

# Create your tests here.

class AccountCreationTestCase(TestCase):
    #create new user - expected to trigger the creation of a linked account
    def setUp(self):
        User.objects.create_user(username="test_user", email="test_user@gmail.com", password="12345")

    # test that an account was made with username matching that of created user
    def test_account_created_for_user(self):
        try:
            user_account = Account.objects.get(username="test_user", email="test_user@gmail.com")
            self.assertEqual(user_account.username, "test_user")
            self.assertEqual(user_account.email, "test_user@gmail.com")
        except:
            self.fail("Failed Test: test_account_created_for_user")

    #test that the user and the account objects are linked
    def test_user_and_account_linked(self):
        try:
            user = User.objects.get(username="test_user")
            user_account = Account.objects.get(user=user)
            self.assertEqual(user, user_account.user)
        except:
            self.fail("Failed Test: test_user_and_account_linked")