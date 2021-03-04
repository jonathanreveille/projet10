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
