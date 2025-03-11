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
    zipcode = forms.CharField(max_length = 10, required = True)

    class Meta:
        model = user_Profile
        fields = ['zipcode', 'phone_number']

    def clean_zipcode(self): # checks if zipcode is valid
        zip_code = self.cleaned_data.get('zipcode')
        if not re.fullmatch(r'\d{5,10}', zip_code): # makes sure zipcode is at least 5 digits long, shorter than 10
            raise forms.ValidationError("Must be atleast 5 digits long (numbers only).")
        return zip_code
    
    def clean_phoneNumber(self): # checks if user's inputted phone number is valid
        phone_number = self.cleaned_data.get('phone_number')
        if not re.fullmatch(r'\d{10}', phone_number): # phone number must be 10 digits long
            raise forms.ValidationError("Must be at least 10 digits long (numbers only).")
        return phone_number