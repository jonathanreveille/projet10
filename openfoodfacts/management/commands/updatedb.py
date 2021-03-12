from django.core.management.base import BaseCommand, CommandError
from datetime import datetime

from openfoodfacts.apiclient import ProductDownloader
from products.models import Product, Category
from openfoodfacts.constant import URL_OFOODFACTS, CATEGORY_LIST


class Command(BaseCommand):
    help='Mise à jour de la database avec des nouvelles données uniquement'

    def handle(self, *args, **options):
        """Method that downloads products from OFF
        API to feed our database with new products
        or with information updates on products"""

        for category in CATEGORY_LIST:
            b = ProductDownloader(URL_OFOODFACTS, category)
            b.search_connexion()
            b.fetch_data_from_API()

            products = b.get_products() #Liste de produit, clean avec chaque key:value

            Product.objects.update_product_fields(category, products)

            with open("cron.log", "a") as log:
                log.write(f"Cron job accomplished with success at : {datetime.now()} \n")