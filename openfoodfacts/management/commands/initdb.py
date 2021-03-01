from django.core.management.base import BaseCommand, CommandError

from openfoodfacts.apiclient import ProductDownloader
from products.models import Product, Category
from openfoodfacts.constant import URL_OFOODFACTS, CATEGORY_LIST


class Command(BaseCommand):
    help = 'Initialise la base de données à partir des données de Openfoodfacts'

    def handle(self, *args, **options):
        """method that adds all products in db"""

        for category in CATEGORY_LIST:
            a = ProductDownloader(URL_OFOODFACTS, category)
            a.search_connexion()
            a.fetch_data_from_API()

            products = a.get_products() #nous avons une liste de produit clean avec chaque champs correspondant

            Product.objects.create_objects_from_openfoodfacts(category, products) #on va créer les objets
            
            # continue
        
        print('Every product is in your database now ! Here you go ! ')

