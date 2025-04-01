from django import forms



class username_form(forms.ModelForm):
    new_Username = forms.CharField(widget=forms.PasswordInput)