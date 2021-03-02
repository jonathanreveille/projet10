import unittest
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.contrib.auth.models import User

class PurbeurreFunctionalSearchTest(StaticLiveServerTestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_search_in_purbeurre_search_bar_firefox(self):
        driver = self.driver
        driver.get("http://localhost:8000/")
        self.assertIn("Purbeurre", driver.title)
        elem = driver.find_element_by_name("query_search")
        elem.send_keys("pizza")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source

    def tearDown(self):
        self.driver.close()

class PurbeurreFunctionalUserLogInTest(StaticLiveServerTestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_user_login_to_existing_account_firefox(self):
        driver = self.driver
        driver.get("http://localhost:8000/login/")
        self.assertIn("Purbeurre - Se connecter", driver.title)
        elem = driver.find_element_by_name("username")
        elem.send_keys("usertest123")
        elem2 = driver.find_element_by_name("password")
        elem2.send_keys("bouyaka231")
        elem2.send_keys(Keys.RETURN)
        assert "fas fa-sign-out-alt" not in driver.page_source
        assert "fas fa-sign-in-alt" in driver.page_source

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

class PurbeurreFunctionalUserCreationTest(StaticLiveServerTestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.user = User.objects.create_user(
            username="usertest123test",
            email="userOctest@comp.com",
            password="bouyaka123",
            )

    def test_new_user_to_create_account_firefox(self):
        driver = self.driver
        driver.get("http://localhost:8000/register/")
        self.assertIn('Purbeurre - Créer un compte', driver.title)
        new_username = driver.find_element_by_name("username")
        new_username.send_keys("usertest123test")
        email = driver.find_element_by_name("email")
        email.send_keys("userOctest@comp.com")
        password1 = driver.find_element_by_name("password1")
        password1.send_keys("bouyaka123")
        password2 = driver.find_element_by_name("password2")
        password2.send_keys("bouyaka123")
        password2.send_keys(Keys.RETURN)
        assert "fas fa-user" not in driver.page_source
        assert "fas fa-carrot" not in driver.page_source

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

class PurbeurreFunctionalUserCanDisconnect(StaticLiveServerTestCase):
    
    def setUp(self):
        driver = webdriver.Firefox()
        self.driver = driver
        self.driver.get("http://localhost:8000/login/")
        elem = self.driver.find_element_by_name("username")
        elem.send_keys("usertest123")
        elem2 = self.driver.find_element_by_name("password")
        elem2.send_keys("bouyaka231")
        elem2.send_keys(Keys.RETURN)

    def test_user_can_disconnect_from_home_page(self):
        self.driver.get("http://localhost:8000/logout/")
        self.assertIn('Purbeurre - Déconnexion', self.driver.title)
        
    def tearDown(self):
        self.driver.close()
        self.driver.quit()

class PurbeurreFunctionalUserSendEmailToPurbeurreHomePage(StaticLiveServerTestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_user_on_homepage_can_send_email_from_homepage(self):
        driver = self.driver
        driver.get("http://localhost:8000/")
        self.assertIn('Purbeurre - Accueil', driver.title)
        elem = driver.find_element_by_name("contact_email")
        elem.click()
        assert "contact_email" in driver.page_source

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == "__main__":
    unittest.main() 