"""Creating forms for users to login"""
from django import forms

class LoginForm(forms.Form):
    """Creating the actual form field view"""
    username = forms.CharField(max_length=25, required=True)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)
    