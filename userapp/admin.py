from django.contrib import admin

# Register your models here.

from .models import UserProfile


class ProfileAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'age',
        'address',
        'image'
    ]


admin.site.register(UserProfile,ProfileAdmin)