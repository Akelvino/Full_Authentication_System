from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

form_design = {
    'class':'text-slate-900 bg-white border border-gray-300 w-full text-sm px-4 py-3 rounded-md outline-blue-500'
}

class UserRegistration(UserCreationForm):
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'placeholder':'Enter your first name',
        **form_design
    }))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'placeholder':'Enter your last name',
        **form_design
    }))
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'placeholder':'Enter your username',
        **form_design
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder':'Enter your email address',
        **form_design
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs=({
        'placeholder': 'Enter your password',
        **form_design
    })))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=({
        'placeholder': 'Confirm your password',
        **form_design
    })))
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password1','password2']