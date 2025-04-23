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
        # if no username is entered
        if not username:
            self.add_error("username", "Please fill out this field.")
        # if username already exists
        if User.objects.filter(username=username).exists():
            self.add_error("username", "This username is already in use.")
        return username

class profile_Form(forms.ModelForm):
    zip_code = forms.CharField(max_length = 10, required = True)
    email_address = forms.CharField(max_length = 256, required = True)
    phone_number = forms.CharField(max_length = 11, required = False)

    class Meta:
        model = user_Profile
        fields = ['zip_code', 'phone_number', 'email_address']

    def clean_zip_code(self): # checks if zip_code is valid
        zip_code = self.cleaned_data.get('zip_code')
        # if no zipcode is entered
        if not zip_code:
            self.add_error("zip_code", "Please fill out this field.")
        # if zipcode isn't between 5 & 10 digits
        if not re.fullmatch(r'\d{5,10}', zip_code):
            self.add_error("zip_code", "Must be between 5 and 10 digits long.")
        return zip_code
        
    def clean_email_address(self): # checks if user's inputted email is valid
        email_address = self.cleaned_data.get('email_address')
        if email_address:
            # if entered email already exists
            if user_Profile.objects.filter(email_address = email_address).exists():
                self.add_error("email_address", "this email is already in use.")
        return email_address
    
    def clean_phone_number(self): # checks if user's inputted phone # is valid (not a duplicate)
        phone_number = self.cleaned_data.get('phone_number')
        if phone_number:
            # if entered phone number is already in use
            if user_Profile.objects.filter(phone_number = phone_number).exists():
                self.add_error("phone_number", "This phone number is already in use.")
            if not re.fullmatch(r'\d{10,12}', phone_number):
                self.add_error("phone_number", "Must be between 10 and 12 digits long.")
        else:
            return None
        return phone_number