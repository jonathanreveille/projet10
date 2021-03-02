from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User


class UsersViewsUnitTest(TestCase):

    def setUp(self):
        User.objects.create_user(
            username="Foodlover12", password="testing123321")

    def test_create_account_page(self):
        """Test if we can have access to register page"""
        response = self.client.get(reverse('register'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed("register/register.html")

    def test_login_page_reverse(self):
        """Test if we can have access to login page"""
        response = self.client.get(reverse('login'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed("register/login.html")
    
    def test_logout_page_reverse(self):
        """Test if we can have access to logout page"""
        response = self.client.get(reverse('logout'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed("register/logout.html")
