from django import forms
from django.contrib.auth.models import User
from .models import user_Profile
import re


class registration_Form(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']
        help_texts = {  # remove default help text
            'username': ''
        }

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("This username is already taken. Please choose another.") # outputs error if inputted username already exists
        return username

class profile_Form(forms.ModelForm):
    zip_code = forms.CharField(max_length = 10, required = True)
    email_address = forms.CharField(max_length = 256, required = True)

    class Meta:
        model = user_Profile
        fields = ['zip_code', 'phone_number', 'email_address']

    def clean_zip_code(self): # checks if zip_code is valid
        zip_code = self.cleaned_data.get('zip_code')
        if not re.fullmatch(r'\d{5,10}', zip_code): # makes sure zipcode is at least 5 digits long, shorter than 10
            raise forms.ValidationError("Must be atleast 5 digits long (numbers only).")
        return zip_code
        
    def clean_email_address(self): # checks if user's inputted email is valid
        email_address = self.cleaned_data.get('email_address')
        if user_Profile.objects.filter(email_address = email_address).exists():
            raise forms.ValidationError("this email is already in use. Please choose another or login with email.")
        return email_address