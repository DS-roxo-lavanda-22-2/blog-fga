from django import forms

class Login(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Passoword', max_length=100)