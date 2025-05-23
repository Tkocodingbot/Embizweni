from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,PasswordChangeForm 
from django.contrib.auth.models import User
from .models import Profile


class LoginForm(AuthenticationForm): # This login form is inherited in urls.py
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': 'True','class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'class':'form-control'}))

class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'autofocus': 'True','class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control'}) )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label='Old Password', widget=forms.PasswordInput(attrs={'autofocus ': 'True', 'autocomplete':'current-password', 'class':'form-control'}))
    new_password1 = forms.CharField(label='New Password', widget=forms.PasswordInput(attrs={'autofocus ': 'True', 'autocomplete':'current-password', 'class':'form-control'}))
    new_password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'autofocus ': 'True', 'autocomplete':'current-password', 'class':'form-control'}))
    
class MyPasswordResetForm(PasswordChangeForm):
    pass

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'mobile', 'city', 'province', 'postal_code' ] 
        Widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'mobile':forms.NumberInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'province':forms.Select(attrs={'class':'form-control'}),
            'postal_code':forms.NumberInput(attrs={'class':'form-control'}),
        }