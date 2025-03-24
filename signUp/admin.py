from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import user_Profile

# Define an inline admin descriptor for user_Profile
class UserProfileInline(admin.StackedInline):
    model = user_Profile
    extra = 0  # Don't show empty fields for new profiles

# Extend the existing UserAdmin to include the profile fields
class CustomUserAdmin(UserAdmin):
    inlines = (UserProfileInline,)  # Add profile fields inside User admin
    list_display = ('username', 'email', 'first_name', 'last_name', 'get_zip_code', 'get_phone_number')  # Customize list display

    def get_zip_code(self, obj):
        return obj.user_profile.zip_code if hasattr(obj, 'user_profile') else "N/A"
    get_zip_code.short_description = "Zip Code"

    def get_phone_number(self, obj):
        return obj.user_profile.phone_number if hasattr(obj, 'user_profile') else "N/A"
    get_phone_number.short_description = "Phone Number"

# Unregister default User admin
admin.site.unregister(User)
# Register User with the new admin class
admin.site.register(User, CustomUserAdmin)
