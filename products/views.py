from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404,render, redirect
from django.urls import reverse
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist

from .models import Product, Favorite
from .forms import SearchedProductForm

#Create your views here
def home(request, search):
    """View of home page of the application purbeurre"""

    form = SearchedProductForm()

    product_search = get_object_or_404(Product, Product.objects.filter(prod_name__icontains=search))
    context = {
        'product': product_search,
        'form': form,
    }

    return render(request, 'products/home.html', context)


def search(request):
    """view that corresponds to the search bar zone,
    that allows to retrieve data from the DB
    according the user's query"""

    context = {}

    if request.method == "GET":
        form = SearchedProductForm(request.GET)

        if form.is_valid():
            product = form.cleaned_data.get("query_search")
            product_found = Product.objects.filter( 
                prod_name__icontains=product,
                prod_nutrition_grade_fr__lt="d",
                )[3:9]

            context = {
                'product':product,
                'product_found': product_found,
            }

        return  render(request, 'products/search.html', context)

    else:
        form = SearchedProductForm()
        context = {
            'form' : form
        }

    return render(request, 'products/home.html', context)


# # new 22102020
def detail(request, product_id):
    """view about detail page of a product"""

    product_details = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product_details
        }
    return render(request, 'products/detail.html', context)


def favorite(request):
    """method to create a favorite object
    from product_id and new substitute"""

    if request.method == "POST":
        user = request.user
        substitute_id = request.POST["favorite_id"]
        product_id = request.POST["id_product"]

        substitute = Product.objects.get(id=substitute_id)
        product_replaced = Product.objects.get(id=product_id)
        
        Favorite.objects.get_or_create(
            user=user,
            substitute=substitute,
            substituted=product_replaced,
        )
        messages.success(request, "Vous avez bien ajouté un nouveau produit dans vos favoris")

        return redirect('products:detail', product_id=substitute_id)
    
    return redirect('home')
