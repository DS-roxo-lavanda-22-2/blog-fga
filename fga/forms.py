from django import forms
from django.forms import ModelForm
from .models import Login

class form_login(ModelForm):
    class Meta:
        model = Login
        fields = ['email', 'password']