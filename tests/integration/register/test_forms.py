from django.test import TestCase

from register.forms import UserRegisterForm

class UsersFormTestCase(TestCase):

    def setUp(self):
        self.form = UserRegisterForm(data={
            "username": "jonzmundo",
            "email": "jonjontest123@test.com",
            "password1": "foodmaniatest",
            "password2": "foodmaniatest"
            })

        self.form_2 = UserRegisterForm(data={
            "username": "jonzmundo",
            "email": "jonjontest123@test.com",
            "password1": "foodmaniatest123",
            "password2": "foodmaniatest321"
            })

        self.form_3 = UserRegisterForm(data={
            "username": "jonzmundo",
            "email": "jontest.com",
            "password1": "foodmaniatest123",
            "password2": "foodmaniatest321"
            })

    def test_user_creation_forms_is_valid(self):
        self.assertTrue(self.form.is_valid())

    def test_user_creation_forms_is_not_valid(self):
        self.assertFalse(self.form_2.is_valid())

    def test_user_fill_in_email_correctly(self):
        self.assertFalse(self.form_3.is_valid())