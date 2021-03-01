from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField() #default required=True

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

        # This class inherits from UserCreationForm
        # Keep all the configuration in one place
        # when we save a user, it  will add it into User model
