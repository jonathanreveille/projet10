from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from products.models import Category, Product, Brand, Favorite


class ProductsViewsUnitTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="Test_user_food",
            email="testadress@purbeurre.com",
            password="testing123testing",
        )

        self.category = Category.objects.create(category_name="biscuit")
        self.brand1 = Brand.objects.create(brand_name="lu")
        self.brand2 = Brand.objects.create(brand_name="bjork")

        self.product1 = Product.objects.create(
                prod_name="belvita pépite chocolat",
                prod_category=self.category,
                prod_brand=self.brand1,
                prod_nutrition_grade_fr="c",
                prod_image_nutrition_url ="https://static.openfoodfacts.org/images/products/762/221/071/3780/ingredients_fr.99.400.jpg",
                prod_url="https://fr.openfoodfacts.org/produit/7622210713780/belvita-chocolat-et-cereales-completes-lu",
                prod_image_url="https://static.openfoodfacts.org/images/products/762/221/071/3780/front_fr.66.400.jpg",
                )

        self.product2 = Product.objects.create(
                prod_name="petit nature - bjork",
                prod_category=self.category,
                prod_brand=self.brand2,
                prod_nutrition_grade_fr="b",
                prod_image_nutrition_url ="https://static.openfoodfacts.org/images/products/229/820/021/027/nutrition_fr.21.400.jpg",
                prod_url="https://fr.openfoodfacts.org/produit/229820021027/p-tit-nature-bjork",
                prod_image_url="https://static.openfoodfacts.org/images/products/229/820/021/027/front_fr.19.400.jpg",
                )

        self.product1_id = self.product1.id
        self.product2_id = self.product2.id

    def test_homepage(self):
        """Test to access to home page and response is 200"""
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_homepage_unexpected_error(self):
        """Test to access to home page with
        error in url and response is 404"""
        response = self.client.get('/home')
        self.assertTrue(response.status_code, 404)

    def test_homepage_reverse(self):
        """Test if we use reverve, we can access to homepage
        returns 200"""
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)

    def test_views_result_search(self):
        """Test if search bar works to see for
        an existing category of products, returns 200"""
        response = self.client.get('/products/search/?query_search=biscuit')
        self.assertEquals(response.status_code, 200)

    def test_views_product_detail_not_registered(self):
        """Test for a search in the url for a product's detail
        sheet, on a product that does NOT exist, returns 404"""
        response = self.client.get('/products/detail/11111111')
        self.assertEquals(response.status_code, 404)