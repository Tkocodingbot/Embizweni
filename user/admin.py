from django.contrib import admin
from . models import Profile


@admin.register(Profile)
class UsersModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'city', 'province', 'postal_code']
