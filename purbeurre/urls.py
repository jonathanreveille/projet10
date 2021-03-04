"""purbeurre URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.views.generic import TemplateView
from register import views as register_views

def trigger_error(request):
    division_by_zero = 1 / 0


urlpatterns = [
    path('', TemplateView.as_view(template_name='products/home.html'), name='home'),
    path('products/', include('products.urls', namespace="products")),
    path('admin/', admin.site.urls),
    path('register/', register_views.register, name='register'),
    path('profile/', register_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='register/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='register/logout.html'), name='logout'),
    path('profile/favorite', register_views.favorites, name="favorite" ),
    path('sentry-debug/', trigger_error),
]