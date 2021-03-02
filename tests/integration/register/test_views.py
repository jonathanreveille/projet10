from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User


class UsersViewsTest(TestCase):

    def setUp(self):
        User.objects.create_user(
            username="Foodlover12", password="testing123321")
        self.client = Client()

    def test_access_to_favorite_page_when_user_is_not_authenticated(self):
        response = self.client.get(reverse('favorite'))
        self.assertEquals(response.status_code, 302)

    def test_see_user_profile_page(self):
        self.client.login(username="Foodlover12", password="testing123321")
        response = self.client.get("/profile/")
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed("register/profile.html")
    
    def test_see_user_favorite_page_from_profile(self):
        self.client.login(username="Foodlover12", password="testing123321")
        response = self.client.get("/profile/favorite")
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed("register/favorite.html")


