from django.contrib import admin
# Register your models here.
from .models import Product, Brand, Category, Favorite

admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(Favorite)

#admin.site.register(Store)
# Store