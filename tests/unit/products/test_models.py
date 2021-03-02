from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from products.models import Category, Brand, Product

class ProductModelsUnitTests(TestCase):

    def setUp(self):
        self.category = Category.objects.create(category_name="biscuit")
        self.brand = Brand.objects.create(brand_name="lu")
        self.product = Product.objects.create(
        prod_name="belvita pépite chocolat",
        prod_category=self.category,
        prod_brand=self.brand,
        prod_nutrition_grade_fr="c",
        prod_image_nutrition_url ="https://static.openfoodfacts.org/images/products/762/221/071/3780/ingredients_fr.99.400.jpg",
        prod_url="https://fr.openfoodfacts.org/produit/7622210713780/belvita-chocolat-et-cereales-completes-lu",
        prod_image_url="https://static.openfoodfacts.org/images/products/762/221/071/3780/front_fr.66.400.jpg",
        )

    def test_if_product_is_created_with_all_fields(self):
        """Test if all fields required fields are accessible
        from the creation of a Product Object"""
        self.assertEquals(self.product.prod_nutrition_grade_fr, "c")
        self.assertEquals(self.product.prod_name, "belvita pépite chocolat")
        self.assertTrue(self.product.prod_category, self.category)
        self.assertTrue(self.product.id, "1")
