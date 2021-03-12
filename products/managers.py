from django import db
from . import models


class ProductManager(db.models.Manager): # pour faire recherche pour tout les produits

    def create_objects_from_openfoodfacts(self, category, product_list):
        """this method is to create product objects into our
        database"""

        category, created = models.Category.objects.get_or_create(category_name=category)

        for product in product_list:
            prod_image_url = product["image_front_url"]
            prod_image_nutrition_url = product["image_nutrition_url"]
            prod_url = product["url"]

            if len(prod_image_url) > 200 or len(prod_image_nutrition_url) > 200 or len(prod_url) > 200:
                continue

            brand, created = models.Brand.objects.get_or_create(brand_name=product["brands"])
            
            product, created = models.Product.objects.get_or_create(
                                prod_url=product["url"],
                                defaults = {
                                    'prod_name' : product["product_name"][:255],
                                    'prod_nutrition_grade_fr' : product["nutrition_grade_fr"],
                                    'prod_image_nutrition_url' : product["image_nutrition_url"],
                                    'prod_image_url' : product["image_front_url"],
                                    'prod_brand' : brand,
                                    'prod_category' : category,
                                    })


    def update_product_fields(self, category, product_list):
        """Method that updates the fields of a specific product
        from Openfoodfacts, or adds a new product that was just
        released"""

        category, created = models.Category.objects.get_or_create(category_name=category)

        for product in product_list:

            try:
                the_product = models.Product.objects.get(prod_url=product["url"])
                the_product.prod_name = product["product_name"]
                the_product.prod_nutrition_grade_fr = product["nutrition_grade_fr"]
                the_product.prod_image_nutrition_url = product["image_nutrition_url"]
                the_product.prod_url = product["url"]
                the_product.prod_image_url = product["image_front_url"]
                the_product.save()

            except models.Product.DoesNotExist:
                prod_image_url = product["image_front_url"]
                prod_image_nutrition_url = product["image_nutrition_url"]
                prod_url = product["url"]

                if len(prod_image_url) > 200 or len(prod_image_nutrition_url) > 200 or len(prod_url) > 200:
                    continue

                brand, created = models.Brand.objects.get_or_create(brand_name=product["brands"])

                product, created = models.Product.objects.get_or_create(
                prod_url=product["url"],
                defaults = {
                    'prod_name' : product["product_name"][:255],
                    'prod_nutrition_grade_fr' : product["nutrition_grade_fr"],
                    'prod_image_nutrition_url' : product["image_nutrition_url"],
                    'prod_image_url' : product["image_front_url"],
                    'prod_brand' : brand,
                    'prod_category' : category,
                    })