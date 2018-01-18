from django.contrib.auth.models import User

from django import forms
from .models import Instructor , Course , Interest


class UserForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)

    #this class is info abt the form
    class Meta:
        model = User

        fields = ['username' , 'email' , 'password']


class InterestForm(forms.ModelForm):

    #this class is info abt the form
    class Meta:
        model = Interest

        fields = ['Name']

class Login(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)

    #this class is info abt the form
    class Meta:
        model = User

        fields = ['username', 'password']
