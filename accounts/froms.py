from django import forms
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget




class RegisterForm(UserCreationForm):

    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={
        'class':'form-control', 'name':'username', 'placeholder':'Username'
    }))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={
        'class':'form-control', 'name':'email', 'placeholder':'Email'
    }))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        'class':'form-control', 'name':'password1', 'placeholder':'Password'
    }))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={
        'class':'form-control', 'name':'password2', 'placeholder':'Confirm Password'
    }))


    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']




class ProfileForm(forms.ModelForm):

    phone = forms.CharField(label='Phone', widget=forms.TextInput(attrs={
    'class':'form-control', 'name':'phone', 'placeholder':'Phone'
    }))
    age = forms.CharField(label='Age', widget=forms.TextInput(attrs={
        'class':'form-control', 'name':'age', 'placeholder':'Age'
    }))
    country = CountryField(blank_label='(select country)').formfield(widget=CountrySelectWidget(attrs={'class':'form-control'
    }))

    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user']




class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']