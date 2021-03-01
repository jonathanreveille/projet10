# Import notre formulaire
from .forms import SearchedProductForm

def search_form(request):
    form =  SearchedProductForm()
    return {'search_form': form}