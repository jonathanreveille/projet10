from django.test import TestCase
from openfoodfacts.apiclient import ProductDownloader

class OpenFoodFactClientApiCreateObjectTest(TestCase):
    """test response from the OpenFoodFact API"""
    def setUp(self):
        self.client = ProductDownloader(url="https://fr.openfoodfacts.org/cgi/search.pl", category="pizza")

    def test_if_object_is_created_with_category_and_url_of_openfoodfact(self):
        self.assertEquals(self.client.url, "https://fr.openfoodfacts.org/cgi/search.pl")
        self.assertEquals(self.client.category, "pizza")

    def test_if_fetch_data_from_API_returns_a_dictionary(self):
        self.client.search_connexion()
        dictionary = self.client.fetch_data_from_API()
        self.assertEquals(type(dictionary), dict)


def test_api_off_response(monkeypatch):
    """test response from the OpenFoodFact API"""

    IMITATION_RESPONSE_OFF_1 = {'product': '',
                                'query':[{"id":"737628064502",
                                        'product_name_fr':'Petit Prince ChocoMax',
                                        'nutrition_grade_fr' : 'c',
                                        'brands':'Lu',
                                        'stores': 'Carrefour',
                                        'url':'https://api.nal.usda.gov/ndb/reports/?ndbno=45108002&type=f&format=json&api_key=DEMO_KEY',
                                        'categories':'biscuit',
                                        'code':"0737628064502",
                                        'image_nutrition_url': "https://static.openfoodfacts.org/images/products/073/762/806/4502/nutrition.6.200.jpg", 
                                        'image_front_url':"https://static.openfoodfacts.org/images/products/073/762/806/4502/front_en.6.200.jpg",
                                        }]}

    class MockRequestsGet:
        def __init__(self, url, params=None):
            pass

        def json(self):
            return IMITATION_RESPONSE_OFF_1

    response = MockRequestsGet
    path = "purbeurre.openfoodfacts.apiclient.ProductDownloader.fetch_data_from_API"
    monkeypatch.setattr(path, response.json)

    assert response.json(IMITATION_RESPONSE_OFF_1) == IMITATION_RESPONSE_OFF_1