from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class user_Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # connects one unique profile with its unique user - - - if one is deleted so is the other
    address = models.CharField(max_length=255, blank=True, null=True) # additional fields added to user continued below
    zip_code = models.CharField(max_length=10) # REQUIRED FIELD***
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.user.username