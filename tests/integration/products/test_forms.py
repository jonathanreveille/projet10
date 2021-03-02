from django.test import TestCase

from products.forms import SearchedProductForm

class SearchedProductFormTest(TestCase):

    def setUp(self):
        self.query = SearchedProductForm()

    def test_unvalid_data(self):
        self.assertFalse(self.query.is_valid())
    
    def test_valid_data(self):
        self.query.query_search = "pizza"
        self.assertEquals(self.query.query_search, "pizza")