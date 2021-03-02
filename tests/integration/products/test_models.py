from django.test import TestCase, TransactionTestCase
from django.contrib.auth.models import User

from products.models import Product, Category, Brand, Favorite

class CategoryModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Category.objects.create(category_name="pizza")

    def setUp(self):
        # Run once for every test method to setup clean data.
        self.category = Category.objects.get(id=1)

    def test_category_name_label(self):
        field_label = self.category._meta.get_field('category_name').verbose_name
        self.assertEquals(field_label, 'category name')

    def test_category_name_max_length(self):
        max_length = self.category._meta.get_field('category_name').max_length
        self.assertEquals(max_length, 255)

    def test_category_name_is_category_name(self):
        expected_object_name = f'{self.category.category_name}'
        self.assertEquals(expected_object_name, str(self.category))
    
    def test_category_verbose_name_plural(self):
        category_plural = str(Category._meta.verbose_name_plural)
        self.assertEquals(category_plural, "categories")

class BrandModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Brand.objects.create(brand_name="sodebo")
    
    def setUp(self):
        # Run once for every test method to setup clean data.
        self.brand = Brand.objects.get(id=1)

    def test_brand_name_label(self):
        field_label = self.brand._meta.get_field('brand_name').verbose_name
        self.assertEquals(field_label, 'brand name')
    
    def test_brand_name_max_length(self):
        max_length = self.brand._meta.get_field('brand_name').max_length
        self.assertEquals(max_length, 255)

    def test_brand_name_is_brand_name(self):
        expected_object_name = f'{self.brand.brand_name}'
        self.assertEquals(expected_object_name, str(self.brand))


class ProductModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        category = Category.objects.create(category_name="pizza")
        # store = Store.objects.create(store_name="u")
        brand = Brand.objects.create(brand_name="sodebo")

        Product.objects.create(
                prod_name="pizza crusty",
                prod_category=category,
                prod_brand=brand,
                prod_nutrition_grade_fr="b",
                prod_image_nutrition_url ="https://static.openfoodfacts.org/images/products/324/227/305/0550/ingredients_fr.23.400.jpg",
                prod_url="https://fr.openfoodfacts.org/produit/3242273050550/sodebo-pizza-crust-farmer",
                prod_image_url="https://static.openfoodfacts.org/images/products/324/227/305/0550/front_fr.16.400.jpg",
                )
    
    def setUp(self):
        # Run once for every test method to setup clean data.
        self.product = Product.objects.get(id=1)
    
    def test_prod_name_label(self):
        field_label = self.product._meta.get_field('prod_name').verbose_name
        self.assertEquals(field_label, 'prod name')

    def test_prod_name_max_length(self):
        max_length = self.product._meta.get_field('prod_name').max_length
        self.assertEquals(max_length, 255)
    
    def test_object_is_product_name_comma_nutrition_grade_fr(self):
        expected_object_name = f'{self.product.prod_name}, nutriscore: {self.product.prod_nutrition_grade_fr}'
        self.assertEquals(expected_object_name, str(self.product))

    def test_nutrition_grade_fr_max_length(self):
        max_length = self.product._meta.get_field('prod_nutrition_grade_fr').max_length
        self.assertEquals(max_length, 1)

    def test_objects_nutrition_grade_fr(self):
        nutrition_grade = self.product.prod_nutrition_grade_fr
        self.assertEquals(nutrition_grade, "b")
    
    def test_objects_prod_name(self):
        product_name = self.product.prod_name
        self.assertEquals(product_name, "pizza crusty")


class ProductTestsThatDependsOnPrimaryKeySequences(TransactionTestCase):
    reset_sequences = True

    def setUp(self):
        category = Category.objects.create(category_name="pizza")
        brand = Brand.objects.create(brand_name="sodebo")

        self.product = Product.objects.create(prod_name="pizza crusty",
                prod_category=category,
                prod_brand=brand,
                prod_nutrition_grade_fr="b",
                prod_image_nutrition_url ="https://static.openfoodfacts.org/images/products/324/227/305/0550/ingredients_fr.23.400.jpg",
                prod_url="https://fr.openfoodfacts.org/produit/3242273050550/sodebo-pizza-crust-farmer",
                prod_image_url="https://static.openfoodfacts.org/images/products/324/227/305/0550/front_fr.16.400.jpg",
                )

    def test_product_pk_is_one(self):
        self.assertEquals(self.product.pk, 1)


class FavoriteModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        category = Category.objects.create(category_name="pizza")
        brand = Brand.objects.create(brand_name="picard")

        product = Product.objects.create(
                prod_name="pizza n11 chevre, miel, noix",
                prod_category=category,
                prod_brand=brand,
                prod_nutrition_grade_fr="d",
                prod_image_nutrition_url ="https://static.openfoodfacts.org/images/products/324/227/305/0550/ingredients_fr.23.400.jpg",
                prod_url="https://fr.openfoodfacts.org/produit/3270160838110/pizza-n-11-chevre-miel-noix-picard",
                prod_image_url="https://static.openfoodfacts.org/images/products/327/016/083/8110/front_fr.27.400.jpg",
                )

        substitute = Product.objects.create(
                prod_name="3 fromages bio",
                prod_category=category,
                prod_brand=brand,
                prod_nutrition_grade_fr="b",
                prod_image_nutrition_url ="https://static.openfoodfacts.org/images/products/327/016/037/1983/nutrition_fr.6.400.jpg",
                prod_url="https://fr.openfoodfacts.org/produit/3270160371983/pizza-3-fromages-bio-picard",
                prod_image_url="https://static.openfoodfacts.org/images/products/327/016/037/1983/front_fr.19.400.jpg",
                )

        user = User.objects.create_user(
            username="Test_user_food",
            email="testadress@purbeurre.com",
        )

        Favorite.objects.create(
            user=user,
            substitute=substitute,
            substituted=product)

    def setUp(self):
        self.favorite = Favorite.objects.get(id=1)

    def test_user_is_user_favorite(self):
        expected_object_user = f'{self.favorite.user}'
        self.assertEquals(expected_object_user, str(self.favorite.user))

    def test_favorite_substitute_is_substitute_selected(self):
        expected_substitute_product = f'{self.favorite.substitute}'
        self.assertEquals(expected_substitute_product, str(self.favorite.substitute))

    def test_favorite_replaced_product_is_replaced_product(self):
        expected_unhealthy_product = f'{self.favorite.substituted}'
        self.assertEquals(expected_unhealthy_product, str(self.favorite.substituted))

    def test_show_how_str_of_favorites(self):
        expected_line = f"new:{self.favorite.substitute}, old:{self.favorite.substituted}"
        self.assertEquals(expected_line, str(self.favorite))