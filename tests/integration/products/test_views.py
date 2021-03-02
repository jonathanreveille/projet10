from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from products.models import Category, Product, Brand, Favorite


class ProductsViewsTest(TestCase):

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


    def test_views_product_favorite_post_method_to_add_substitute_and_substituted(self):
        self.client.login(username=self.user.username, password=self.user.password)
        self.substitute = Product.objects.get(id=self.product1_id)
        self.substituted = Product.objects.get(id=self.product2_id)

        self.fav = Favorite.objects.create(
            user=self.user,
            substitute=self.product1,
            substituted=self.product2,
        )
        self.favorite = Favorite.objects.get(user=self.user)

        self.client.post('profile/favorite',
                                        {
                                        "substitute": self.substitute,
                                        "substituted": self.substituted,
                                        })

        self.assertEquals(self.favorite.substitute.id, self.product1_id)
        self.assertEquals(self.favorite.substituted.id, self.product2_id)

    def test_access_views_favorite_without_account(self):
        response = self.client.get('/profile/favorite/')
        self.assertEquals(response.status_code, 404)