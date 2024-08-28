from django.contrib import admin

# Register your models here.

from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'first_name', 'last_name']
    list_filter =['email']

admin.site.register(User, UserAdmin)