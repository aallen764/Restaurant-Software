from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import user_Profile

class UserProfileInline(admin.StackedInline):
    model = user_Profile
    extra = 0  # don't show empty fields for new profiles

# Extend the existing UserAdmin to include the profile fields
class CustomUserAdmin(UserAdmin):
    inlines = (UserProfileInline,)  # adds the new profile fields under the 'Users' tab in admin page
    list_display = ('username', 'get_email_address', 'first_name', 'last_name', 'get_zip_code', 'get_phone_number')

    def get_zip_code(self, obj):
        return obj.user_profile.zip_code if hasattr(obj, 'user_profile') else "N/A"
    get_zip_code.short_description = "Zip Code"

    def get_phone_number(self, obj):
        return obj.user_profile.phone_number if hasattr(obj, 'user_profile') else "N/A"
    get_phone_number.short_description = "Phone Number"

    def get_email_address(self, obj):
        return obj.user_profile.email_address if hasattr(obj, 'user_profile') else "N/A"
    get_email_address.short_description = "Email Address"

# Unregister default User admin and then re-register the same user using the NEW admin class containing the new profile fields
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
