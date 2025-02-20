from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from register.models import ProductModel, UserModel


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=40, required=True)
    last_name = forms.CharField(max_length=40, required=True)

    class Meta:
        model = UserModel
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=40, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)


class ProductModelForm(forms.ModelForm):
    class Meta:
        model = ProductModel
        fields = '__all__'
