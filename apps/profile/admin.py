from django.contrib import admin
from apps.profile.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['email', 'phone', 'is_active']