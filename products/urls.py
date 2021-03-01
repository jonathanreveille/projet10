from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = "products"

urlpatterns = [
    # ex : /products/search/
    path('search/', views.search, name="search"),
    path('detail/<int:product_id>', views.detail, name='detail'),
    path('favorite/', views.favorite, name="favorite")
]