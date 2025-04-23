from django import forms


from signUp.models import user_Profile

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = user_Profile
        fields = ['zip_code', 'email_address', 'phone_number', 'profile_picture']