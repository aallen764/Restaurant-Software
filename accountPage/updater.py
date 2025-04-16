from django.contrib.auth.models import User
from signUp.models import user_Profile
from django.contrib.auth.hashers import make_password
import re

def update_username(user_id, new_username):
    try:
        user = User.objects.get(id=user_id)
        if User.objects.filter(username=new_username).exclude(pk=user.id).exists():
            return "Username already taken."
        user.username = new_username
        user.save()
        return "Username updated successfully."
    except User.DoesNotExist:
        return "User not found."


def update_password(user_id, new_password):
    try:
        user = User.objects.get(id=user_id)
        user.password = make_password(new_password)
        user.save()
        return "Password updated successfully."
    except User.DoesNotExist:
        return "User not found."


def update_email(user_id, new_email):
    try:
        user = User.objects.get(id=user_id)
        profile = user.user_profile
        if user_Profile.objects.filter(email_address=new_email).exclude(user=user).exists():
            return "Email already in use."
        profile.email_address = new_email
        profile.save()
        return "Email updated successfully."
    except User.DoesNotExist:
        return "User not found."
    except user_Profile.DoesNotExist:
        return "User profile not found."


def update_phone(user_id, new_phone):
    try:
        user = User.objects.get(id=user_id)
        profile = user.user_profile
        if user_Profile.objects.filter(phone_number=new_phone).exclude(user=user).exists():
            return "Phone number already in use."
        profile.phone_number = new_phone
        profile.save()
        return "Phone number updated successfully."
    except User.DoesNotExist:
        return "User not found."
    except user_Profile.DoesNotExist:
        return "User profile not found."


def update_zip(user_id, new_zip):
    try:
        if not re.fullmatch(r'\d{5,10}', new_zip):
            return "Invalid zip code format. Must be 5–10 digits."
        user = User.objects.get(id=user_id)
        profile = user.user_profile
        profile.zip_code = new_zip
        profile.save()
        return "Zip code updated successfully."
    except User.DoesNotExist:
        return "User not found."
    except user_Profile.DoesNotExist:
        return "User profile not found."
