from django import forms
####USER PAGE VVVVV
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
#^^^^^^^


        #####################USER PAGE   VVVVVVVVVVVVVV

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


