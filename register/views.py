from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import UserRegisterForm
from products.models import Favorite

def register(request):

    if request.method  == "POST":
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            messages.success(request, f'Votre compte a été créé avec succès {username} avec adresse {email}! Vous pouvez maintenant vous connecter')
            return redirect('login')

    else:

        form = UserRegisterForm()
    return render(request, 'register/register.html', {'form':form})

@login_required
def profile(request):
    return render(request, 'register/profile.html')

@login_required
def favorites(request):
    """method to show favorites of user's"""
    
    user = request.user
    user_favorites = Favorite.objects.filter(user=user)
    substitutes = [favorite.substitute for favorite in user_favorites]

    context = {
        'user': user,
        'substitutes': substitutes,
    }

    return render(request, 'register/favorite.html', context)



# @login_required
# def favorites(request):
#     """method to show favorite section
#     of the users"""

#     user = request.user
#     favorites = Favorite.objects.filter(user=user)
    
#     n = 0
#     while n != len(favorites):
#         substitutes = list()
#         substitute = favorites[0].substitute
#         substitutes.append(substitute)
#         n += 1

#         return substitutes

#     context = {
#         'user':user,
#         'substitutes': substitutes,
#     }

#     return render(request, 'register/favorite.html', context)



# @login_required
# def favorites(request):
#     """ Create favorite page from a User'id """

#     substitutes = []

#     user = request.user
#     favorites_of_user = Favorite.objects.filter(user=user)
#     print(len(favorites_of_user))

#     for substitute in favorites_of_user:
#         subsitute_1 = favorite[0].substitute
#         subsitutes.append(substitute_1)

#     context = {
#         'user' : user,
#         'substitutes' : substitutes,
#     }

#     return render(request, 'register/favorite.html', context)


# @login_required
# def favorites(request):
#     """ Create favorite page from a User'id """
    
#     substitutes_query_set = []
#     substitutes = []

#     user = request.user
#     user_set_favorite = Favorite.objects.filter(user=user).values('substitute')
#     substitutes_query_set.append(user_set_favorite)
#     print("DEBUG1 : ", substitutes_query_set)

#     for substitute in substitutes_query_set:
#         for value in substitute:
#             substitutes.append(value)

#         context = {
#             'user' : user,
#             'substitutes':substitutes,
#         }

#     return render(request, 'register/favorite.html', context)

# @login_required
# def favorites(request):
#     """ Create favorite page from a User'id """
    
#     substi = []
#     user = request.user
#     user_set_favorite = Favorite.objects.filter(user=user).values('substitute')
#     substi.append(user_set_favorite)
    
#     for substitutes in user_set_favorite:
#         for value in substitutes:
#             substi.append(value)

#         context = {
#             'user' : user,
#             'substitutes':substi,
#         }

#     return render(request, 'register/favorite.html', context)




## NOTES ##
    # try to find a way to get the product from the 
    # code of the substitute

    # for substitute in substitutes:
    #   Trouve le produit avec le meme id
    #   ajoute le dans une liste vide avec append
    #   cela devient substitutes en sortie qui sont des produits

    
    
    # substitutes = [substitute for substitute in favorites_of_user]


    # favorites = Favorite.objects.all()
    # substitutes = [favorites[0].substitute for substitute in favorites_of_user]


#OPTIONS of messages that pops up once after specific action
#messages.debug
#messages.info
#messages.success
#messages.warning
#messages.error