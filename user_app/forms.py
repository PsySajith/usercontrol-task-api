from django import forms
from django.contrib.auth.models import User


class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100,widget=forms.PasswordInput)


# - The User model’s password field is a CharField, but by default Django will
#  render it as a plain text input.
# - That’s insecure and not user-friendly — you don’t want passwords visible
#  while typing.
# - Fixing it with a widget
# - By explicitly declaring password = forms.CharField(widget=forms.PasswordInput), you override the default behavior.
