from django import forms
from .models import Book
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'Author', 'Price']


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    role = forms.ChoiceField(choices=User.ROLES, required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'role', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Email')