from django.contrib.auth.models import User

from django import forms


class UserForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)

    #this class is info abt the form
    class Meta:
        model = User

        fields = ['username' , 'email' , 'password']