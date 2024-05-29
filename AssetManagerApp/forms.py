from dataclasses import fields
from turtle import textinput
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import UserLog
from .models import Space
from .models import SpaceMemberManagment
from django import forms

from django.forms.widgets import PasswordInput, TextInput


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())
    
class UserLogForm(forms.ModelForm):
    class Meta:
        model = UserLog
        fields = ['title','information']

class CreateSpaceForm(forms.ModelForm):
    class Meta:
        model = Space
        fields = ['name']
        
class EditSpaceForm(forms.ModelForm):
    class Meta:
        model = Space
        fields = ['name']
   
# saving of lookup table that ties space and user together is working but not reflecting on edit
# could move share panel elsewhere        
class ShareSpaceForm(forms.ModelForm):
    space = forms.ModelChoiceField(
        queryset=Space.objects.all(),
        to_field_name='id',
        required=True,  
        widget=forms.Select(attrs={'class': 'form-control'})
    )
     
    user = forms.ModelChoiceField(
        queryset=User.objects.all(),
        to_field_name='id',
        required=True,  
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    class Meta:
        model = SpaceMemberManagment
        fields = ['space', 'user']
