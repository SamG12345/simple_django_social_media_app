from django.contrib import admin
from .models import Profile, Lekh

# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user']

@admin.register(Lekh)
class lekhAdmin(admin.ModelAdmin):
    list_display = ['profile', 'body', 'file']
# Note: 'user' in list_display assumes you have a __str__ method in your User model.
# If not, you might want to display a different attribute or define __str__ in your User model.
