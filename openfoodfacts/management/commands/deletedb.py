from django.core.management.base import BaseCommand, CommandError

from products.models import Product, Category, Favorite, Brand

class Command(BaseCommand):
    help = 'Efface toute la base de données du projet'

    def handle(self, *args, **options):
        Category.objects.all().delete()
        Brand.objects.all().delete()
        Product.objects.all().delete()
        Favorite.objects.all().delete()


        # Store.objects.all().delete()

