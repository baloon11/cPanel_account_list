# -*- coding: utf-8 -*-
from django import forms

class StartForm(forms.Form):
    username = forms.CharField(max_length=300,label='Username')
    password= forms.CharField(max_length=300,label='Password',widget=forms.PasswordInput())