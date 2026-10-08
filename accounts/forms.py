from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Address
class RegisterForm(UserCreationForm):
    class Meta: model=User; fields=('username','email','first_name','last_name','phone','password1','password2')
class AddressForm(forms.ModelForm):
    class Meta: model=Address; fields='__all__'; exclude=('user',)
